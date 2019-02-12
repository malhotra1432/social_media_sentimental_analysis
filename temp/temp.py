from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import sys
import tweepy
import json
from textblob import TextBlob
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def index(request):
    return HttpResponse("Twitter Data Analysis")

# Getting twitter credentials
def get_twitter_auth():
    try:
        CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
        CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET
        ACCESS_TOKEN = settings.TWITTER_ACCESS_TOKEN
        ACCESS_KEY = settings.TWITTER_ACCESS_KEY
    except KeyError:
        sys.stderr.write("TWITTER ENV VARIABLE NOT SET \n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_KEY)
    return auth

# Getting twitter client auth
def get_twitter_client():
    auth = get_twitter_auth()
    client = tweepy.API(auth)
    return client

# Getting tweets with matching hashtag
def get_CSK_hashtag_tweets():
    client = get_twitter_client()
    #search_text = input("Enter keywords/hashtag to search about: ")
    #how_many_tweets = int(input("Enter how many tweets to analyze"))
    positive = 0
    negative = 0
    neutral =  0
    overall_polarity = 0 
    overall_tweet_sentiment = ''
    how_many_tweets = 20
    search_text = "#CSK"
    tweets_data = []
    #tweets_data_json = []
    try:
        for page in tweepy.Cursor(client.search, q=search_text, count=200, since="2018-12-01").items(how_many_tweets):
            #print(page._json)
            tweets_data_list = {}
            blob = TextBlob(page._json['text'])
            for sentence in blob.sentences:
                #print(sentence)
                overall_polarity += sentence.sentiment.polarity 
                tweet_polarity = sentence.sentiment.polarity
                if(tweet_polarity  == 0 or 0.00 or 0.0):
                    neutral += 1
                elif(tweet_polarity < 0 or 0.00 or 0.0):
                    negative += 1
                elif (tweet_polarity > 0 or 0.00 or 0.0):
                    positive += 1    
            if(overall_polarity == 0 or 0.00 or 0.0):
                #print("NEUTRAL")
                overall_tweet_sentiment = "NEUTRAL"
            elif(overall_polarity < 0 or 0.00 or 0.0):
                #print("NEGATIVE")   
                overall_tweet_sentiment = "NEGATIVE"    
            elif(overall_polarity > 0 or 0.00 or 0.0):
                #print("POSITIVE") 
                overall_tweet_sentiment = "POSITIVE"
            tweets_data_list['created_at'] = page._json['created_at']
            tweets_data_list['tweet'] = page._json['text']
            tweets_data_list['polarity'] = tweet_polarity
            tweets_data_list['urls'] = page._json['entities']['urls']
            tweets_data_list['lang'] = page._json['lang']
            tweets_data.append(tweets_data_list)  
            print("=-=-=-==-",tweets_data)
        how_many_tweets = positive + negative + neutral
        positive_percentage = percentage(positive,how_many_tweets)
        negative_percentage = percentage(negative,how_many_tweets)
        neutral_percentage = percentage(neutral,how_many_tweets)
        print("-===-=-=--",positive_percentage,negative_percentage,neutral_percentage,overall_tweet_sentiment)
        labels = ['Positive['+str(positive_percentage)+'%]','Negative['+str(negative_percentage)+'%]','Neutral['+str(neutral_percentage)+'%]']
        sizes = [positive_percentage,negative_percentage,neutral_percentage]
        colors = ['#FFA500','#FFD700','#DAA520']
        patches , texts = plt.pie(sizes,colors = colors,startangle = 90)
        plt.legend(patches,labels,loc="best")
        plt.title('Sentiment')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    except tweepy.error.TweepError as et:
        print(et)
    except Exception as e:
        print(e)
    #print("=-=-=-=-=-",tweets_data)    
    return tweets_data

# Getting top ten tweets
def top_ten_CSK_tweets(request):
    data = get_CSK_hashtag_tweets()
    top_tweets = sorted(data, key=itemgetter('polarity'), reverse=True)
    top_ten_tweets = top_tweets[0:10]
    return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# Plotting graph for top ten tweets
def top_ten_CSK_tweets_graph(request):
    data = get_CSK_hashtag_tweets()
    top_tweets = sorted(data, key=itemgetter('polarity'), reverse=True)
    top_ten_tweets = top_tweets[0:10]
    top_ten_pol = []
    top_ten_text = []
    top_ten_user = []
    #graph_data = []
    #print(top_tweets)
    for i in top_ten_tweets:
        #print(i['polarity'],i['tweet'])
        top_ten_pol.append(i['polarity'])
        top_ten_text.append(i['tweet'])
        top_ten_user.append(i['urls'])  
    return render(request, 'hashtags_tweets.html', {"data": [top_ten_pol,top_ten_text,top_ten_user]})

# Getting tweets from timeline
def get_timeline_tweets(request):
    client = get_twitter_client()
    tweets_data = []
    for status in tweepy.Cursor(client.home_timeline).items(10):
        # print(status.text)
        tweets_data.append(status.text)
    print(tweets_data[0])
    return render(request, 'timeline_tweets.html', {"data": tweets_data})

# Calculating percentage for tweet sentiments
def percentage(part,whole):
    return 100 * float(part) / float(whole)



