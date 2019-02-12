# def index(request):
#     return HttpResponse("Twitter Data Analysis")

# ####################################################################################################################################
# #                                                     AUTHENTICATION 
# # Getting twitter credentials
# def get_twitter_auth():
#     try:
#         CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
#         CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET
#         ACCESS_TOKEN = settings.TWITTER_ACCESS_TOKEN
#         ACCESS_KEY = settings.TWITTER_ACCESS_KEY
#     except KeyError:
#         sys.stderr.write("TWITTER ENV VARIABLE NOT SET \n")
#         sys.exit(1)
#     auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#     auth.set_access_token(ACCESS_TOKEN, ACCESS_KEY)
#     return auth

# # Getting twitter client auth
# def get_twitter_client():
#     auth = get_twitter_auth()
#     client = tweepy.API(auth)
#     return client

# ####################################################################################################################################
# #                                                     CSK HASHTAG DATA

# # Getting tweets with matching hashtag
# def get_CSK_hashtag_tweets():
#     client = get_twitter_client()
#     #search_text = input("Enter keywords/hashtag to search about: ")
#     #how_many_tweets = int(input("Enter how many tweets to analyze"))
#     positive = 0
#     negative = 0
#     neutral =  0
#     overall_polarity = 0 
#     overall_tweet_sentiment = ''
#     how_many_tweets = 200
#     search_text = "#CSK"
#     tweets_data = []
#     tweets_data_json = {}
#     tweets_data_json_list = []
#     tweets_data_list = []
#     try:
#         for page in tweepy.Cursor(client.search, q=search_text, count=200, since="2018-12-01").items(how_many_tweets):
#             tweets_data_dict = {}
#             blob = TextBlob(page._json['text'])
#             for sentence in blob.sentences:
#                 overall_polarity += sentence.sentiment.polarity 
#                 tweet_polarity = sentence.sentiment.polarity
#                 if(tweet_polarity  == 0 or 0.00 or 0.0):
#                     neutral += 1
#                 elif(tweet_polarity < 0 or 0.00 or 0.0):
#                     negative += 1
#                 elif (tweet_polarity > 0 or 0.00 or 0.0):
#                     positive += 1    
#             if positive > negative:
#                 overall_tweet_sentiment = "POSITIVE"
#             elif negative > positive:
#                 overall_tweet_sentiment = "NEGATIVE"   
#             elif negative == positive:
#                 overall_tweet_sentiment = "NEUTRAL" 
#             tweets_data_dict['created_at'] = page._json['created_at']
#             tweets_data_dict['tweet'] = page._json['text']
#             tweets_data_dict['polarity'] = tweet_polarity
#             tweets_data_dict['urls'] = page._json['entities']['urls']
#             tweets_data_dict['lang'] = page._json['lang']
#             tweets_data_list.append(tweets_data_dict)
#         tweets_data.append(tweets_data_list)
#         tweets_data_json['total_tweets'] = positive + negative + neutral
#         tweets_data_json['positive_percentage'] = percentage(positive,tweets_data_json['total_tweets'])
#         tweets_data_json['negative_percentage'] = percentage(negative,tweets_data_json['total_tweets'])
#         tweets_data_json['neutral_percentage'] = percentage(neutral,tweets_data_json['total_tweets'])
#         tweets_data_json['overall_tweet_sentiment'] = overall_tweet_sentiment
#         tweets_data_json_list.append(tweets_data_json)
#         tweets_data.append(tweets_data_json_list)
#     except tweepy.error.TweepError as et:
#         print(et)
#     except Exception as e:
#         print(e)  
#     return tweets_data

# # Getting top ten tweets
# def top_ten_CSK_tweets(request):
#     data = get_CSK_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting top ten tweets
# def top_ten_CSK_tweets_graph(request):
#     data = get_CSK_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-",data[1][0])
#     positive_percentage = data[1][0]['positive_percentage']
#     negative_percentage = data[1][0]['negative_percentage']
#     neutral_percentage = data[1][0]['neutral_percentage']
#     overall_tweet_sentiment = data[1][0]['overall_tweet_sentiment']
#     labels = ['Positive['+str(positive_percentage)+'%]','Negative['+str(negative_percentage)+'%]','Neutral['+str(neutral_percentage)+'%]']
#     sizes = [positive_percentage,negative_percentage,neutral_percentage]
#     colors = ['#FFA500','#FFD700','#DAA520']
#     patches , texts = plt.pie(sizes,colors = colors,startangle = 90)
#     plt.legend(patches,labels,loc="best")
#     plt.title('Sentiment')
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.show()  
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting tweets from timeline
# def get_CSK_timeline_tweets(request):
#     client = get_twitter_client()
#     tweets_data = []
#     for status in tweepy.Cursor(client.home_timeline).items(10):
#         # print(status.text)
#         tweets_data.append(status.text)
#     print(tweets_data[0])
#     return render(request, 'timeline_tweets.html', {"data": tweets_data})

# ####################################################################################################################################

# #                                                     RCB HASHTAG DATA

# # Getting tweets with matching hashtag
# def get_RCB_hashtag_tweets():
#     client = get_twitter_client()
#     #search_text = input("Enter keywords/hashtag to search about: ")
#     #how_many_tweets = int(input("Enter how many tweets to analyze"))
#     positive = 0
#     negative = 0
#     neutral =  0
#     overall_polarity = 0 
#     overall_tweet_sentiment = ''
#     how_many_tweets = 200
#     search_text = "#RCB"
#     tweets_data = []
#     tweets_data_json = {}
#     tweets_data_json_list = []
#     tweets_data_list = []
#     try:
#         for page in tweepy.Cursor(client.search, q=search_text, count=200, since="2018-12-01").items(how_many_tweets):
#             tweets_data_dict = {}
#             blob = TextBlob(page._json['text'])
#             for sentence in blob.sentences:
#                 overall_polarity += sentence.sentiment.polarity 
#                 tweet_polarity = sentence.sentiment.polarity
#                 if(tweet_polarity  == 0 or 0.00 or 0.0):
#                     neutral += 1
#                 elif(tweet_polarity < 0 or 0.00 or 0.0):
#                     negative += 1
#                 elif (tweet_polarity > 0 or 0.00 or 0.0):
#                     positive += 1    
#             if positive > negative:
#                 overall_tweet_sentiment = "POSITIVE"
#             elif negative > positive:
#                 overall_tweet_sentiment = "NEGATIVE"   
#             elif negative == positive:
#                 overall_tweet_sentiment = "NEUTRAL" 
#             tweets_data_dict['created_at'] = page._json['created_at']
#             tweets_data_dict['tweet'] = page._json['text']
#             tweets_data_dict['polarity'] = tweet_polarity
#             tweets_data_dict['urls'] = page._json['entities']['urls']
#             tweets_data_dict['lang'] = page._json['lang']
#             tweets_data_list.append(tweets_data_dict)
#         tweets_data.append(tweets_data_list)
#         tweets_data_json['total_tweets'] = positive + negative + neutral
#         tweets_data_json['positive_percentage'] = percentage(positive,tweets_data_json['total_tweets'])
#         tweets_data_json['negative_percentage'] = percentage(negative,tweets_data_json['total_tweets'])
#         tweets_data_json['neutral_percentage'] = percentage(neutral,tweets_data_json['total_tweets'])
#         tweets_data_json['overall_tweet_sentiment'] = overall_tweet_sentiment
#         tweets_data_json_list.append(tweets_data_json)
#         tweets_data.append(tweets_data_json_list)
#     except tweepy.error.TweepError as et:
#         print(et)
#     except Exception as e:
#         print(e)  
#     return tweets_data

# # Getting top ten tweets
# def top_ten_RCB_tweets(request):
#     data = get_RCB_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-=-RCB",top_ten_tweets)
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting top ten tweets
# def top_ten_RCB_tweets_graph(request):
#     data = get_RCB_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-",data[1][0])
#     positive_percentage = data[1][0]['positive_percentage']
#     negative_percentage = data[1][0]['negative_percentage']
#     neutral_percentage = data[1][0]['neutral_percentage']
#     overall_tweet_sentiment = data[1][0]['overall_tweet_sentiment']
#     labels = ['Positive['+str(positive_percentage)+'%]','Negative['+str(negative_percentage)+'%]','Neutral['+str(neutral_percentage)+'%]']
#     sizes = [positive_percentage,negative_percentage,neutral_percentage]
#     colors = ['#FFA500','#FFD700','#DAA520']
#     patches , texts = plt.pie(sizes,colors = colors,startangle = 90)
#     plt.legend(patches,labels,loc="best")
#     plt.title('Sentiment')
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.show()  
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting tweets from timeline
# def get_RCB_timeline_tweets(request):
#     client = get_twitter_client()
#     tweets_data = []
#     for status in tweepy.Cursor(client.home_timeline).items(10):
#         # print(status.text)
#         tweets_data.append(status.text)
#     print(tweets_data[0])
#     return render(request, 'timeline_tweets.html', {"data": tweets_data})

# ####################################################################################################################################
# #                                                     KKR HASHTAG DATA

# # Getting tweets with matching hashtag
# def get_KKR_hashtag_tweets():
#     client = get_twitter_client()
#     #search_text = input("Enter keywords/hashtag to search about: ")
#     #how_many_tweets = int(input("Enter how many tweets to analyze"))
#     positive = 0
#     negative = 0
#     neutral =  0
#     overall_polarity = 0 
#     overall_tweet_sentiment = ''
#     how_many_tweets = 200
#     search_text = "#KKR"
#     tweets_data = []
#     tweets_data_json = {}
#     tweets_data_json_list = []
#     tweets_data_list = []
#     try:
#         for page in tweepy.Cursor(client.search, q=search_text, count=200, since="2018-12-01").items(how_many_tweets):
#             tweets_data_dict = {}
#             blob = TextBlob(page._json['text'])
#             for sentence in blob.sentences:
#                 overall_polarity += sentence.sentiment.polarity 
#                 tweet_polarity = sentence.sentiment.polarity
#                 if(tweet_polarity  == 0 or 0.00 or 0.0):
#                     neutral += 1
#                 elif(tweet_polarity < 0 or 0.00 or 0.0):
#                     negative += 1
#                 elif (tweet_polarity > 0 or 0.00 or 0.0):
#                     positive += 1    
#             if positive > negative:
#                 overall_tweet_sentiment = "POSITIVE"
#             elif negative > positive:
#                 overall_tweet_sentiment = "NEGATIVE"   
#             elif negative == positive:
#                 overall_tweet_sentiment = "NEUTRAL" 
#             tweets_data_dict['created_at'] = page._json['created_at']
#             tweets_data_dict['tweet'] = page._json['text']
#             tweets_data_dict['polarity'] = tweet_polarity
#             tweets_data_dict['urls'] = page._json['entities']['urls']
#             tweets_data_dict['lang'] = page._json['lang']
#             tweets_data_list.append(tweets_data_dict)
#         tweets_data.append(tweets_data_list)
#         tweets_data_json['total_tweets'] = positive + negative + neutral
#         tweets_data_json['positive_percentage'] = percentage(positive,tweets_data_json['total_tweets'])
#         tweets_data_json['negative_percentage'] = percentage(negative,tweets_data_json['total_tweets'])
#         tweets_data_json['neutral_percentage'] = percentage(neutral,tweets_data_json['total_tweets'])
#         tweets_data_json['overall_tweet_sentiment'] = overall_tweet_sentiment
#         tweets_data_json_list.append(tweets_data_json)
#         tweets_data.append(tweets_data_json_list)
#     except tweepy.error.TweepError as et:
#         print(et)
#     except Exception as e:
#         print(e)  
#     return tweets_data

# # Getting top ten tweets
# def top_ten_KKR_tweets(request):
#     data = get_KKR_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-=-KKR",top_ten_tweets)
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting top ten tweets
# def top_ten_KKR_tweets_graph(request):
#     data = get_KKR_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-",data[1][0])
#     positive_percentage = data[1][0]['positive_percentage']
#     negative_percentage = data[1][0]['negative_percentage']
#     neutral_percentage = data[1][0]['neutral_percentage']
#     overall_tweet_sentiment = data[1][0]['overall_tweet_sentiment']
#     labels = ['Positive['+str(positive_percentage)+'%]','Negative['+str(negative_percentage)+'%]','Neutral['+str(neutral_percentage)+'%]']
#     sizes = [positive_percentage,negative_percentage,neutral_percentage]
#     colors = ['#FFA500','#FFD700','#DAA520']
#     patches , texts = plt.pie(sizes,colors = colors,startangle = 90)
#     plt.legend(patches,labels,loc="best")
#     plt.title('Sentiment')
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.show()  
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting tweets from timeline
# def get_KKR_timeline_tweets(request):
#     client = get_twitter_client()
#     tweets_data = []
#     for status in tweepy.Cursor(client.home_timeline).items(10):
#         # print(status.text)
#         tweets_data.append(status.text)
#     print(tweets_data[0])
#     return render(request, 'timeline_tweets.html', {"data": tweets_data})


# ####################################################################################################################################
# #                                                     MI HASHTAG DATA

# # Getting tweets with matching hashtag
# def get_MI_hashtag_tweets():
#     client = get_twitter_client()
#     #search_text = input("Enter keywords/hashtag to search about: ")
#     #how_many_tweets = int(input("Enter how many tweets to analyze"))
#     positive = 0
#     negative = 0
#     neutral =  0
#     overall_polarity = 0 
#     overall_tweet_sentiment = ''
#     how_many_tweets = 200
#     search_text = "#mumbaiindians"
#     tweets_data = []
#     tweets_data_json = {}
#     tweets_data_json_list = []
#     tweets_data_list = []
#     try:
#         for page in tweepy.Cursor(client.search, q=search_text, count=200, since="2018-12-01").items(how_many_tweets):
#             tweets_data_dict = {}
#             blob = TextBlob(page._json['text'])
#             for sentence in blob.sentences:
#                 overall_polarity += sentence.sentiment.polarity 
#                 tweet_polarity = sentence.sentiment.polarity
#                 if(tweet_polarity  == 0 or 0.00 or 0.0):
#                     neutral += 1
#                 elif(tweet_polarity < 0 or 0.00 or 0.0):
#                     negative += 1
#                 elif (tweet_polarity > 0 or 0.00 or 0.0):
#                     positive += 1    
#             if positive > negative:
#                 overall_tweet_sentiment = "POSITIVE"
#             elif negative > positive:
#                 overall_tweet_sentiment = "NEGATIVE"   
#             elif negative == positive:
#                 overall_tweet_sentiment = "NEUTRAL" 
#             tweets_data_dict['created_at'] = page._json['created_at']
#             tweets_data_dict['tweet'] = page._json['text']
#             tweets_data_dict['polarity'] = tweet_polarity
#             tweets_data_dict['urls'] = page._json['entities']['urls']
#             tweets_data_dict['lang'] = page._json['lang']
#             tweets_data_list.append(tweets_data_dict)
#         tweets_data.append(tweets_data_list)
#         tweets_data_json['total_tweets'] = positive + negative + neutral
#         tweets_data_json['positive_percentage'] = percentage(positive,tweets_data_json['total_tweets'])
#         tweets_data_json['negative_percentage'] = percentage(negative,tweets_data_json['total_tweets'])
#         tweets_data_json['neutral_percentage'] = percentage(neutral,tweets_data_json['total_tweets'])
#         tweets_data_json['overall_tweet_sentiment'] = overall_tweet_sentiment
#         tweets_data_json_list.append(tweets_data_json)
#         tweets_data.append(tweets_data_json_list)
#     except tweepy.error.TweepError as et:
#         print(et)
#     except Exception as e:
#         print(e)  
#     return tweets_data

# # Getting top ten tweets
# def top_ten_MI_tweets(request):
#     data = get_MI_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-=-KKR",top_ten_tweets)
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting top ten tweets
# def top_ten_MI_tweets_graph(request):
#     data = get_MI_hashtag_tweets()
#     top_tweets = sorted(data[0], key=itemgetter('polarity'), reverse=True)
#     top_ten_tweets = top_tweets[0:10]
#     print("=-=-=-=-",data[1][0])
#     positive_percentage = data[1][0]['positive_percentage']
#     negative_percentage = data[1][0]['negative_percentage']
#     neutral_percentage = data[1][0]['neutral_percentage']
#     overall_tweet_sentiment = data[1][0]['overall_tweet_sentiment']
#     labels = ['Positive['+str(positive_percentage)+'%]','Negative['+str(negative_percentage)+'%]','Neutral['+str(neutral_percentage)+'%]']
#     sizes = [positive_percentage,negative_percentage,neutral_percentage]
#     colors = ['#FFA500','#FFD700','#DAA520']
#     patches , texts = plt.pie(sizes,colors = colors,startangle = 90)
#     plt.legend(patches,labels,loc="best")
#     plt.title('Sentiment')
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.show()  
#     return render(request, 'hashtags_tweets.html', {"data": top_ten_tweets})

# # Getting tweets from timeline
# def get_MI_timeline_tweets(request):
#     client = get_twitter_client()
#     tweets_data = []
#     for status in tweepy.Cursor(client.home_timeline).items(10):
#         # print(status.text)
#         tweets_data.append(status.text)
#     print(tweets_data[0])
#     return render(request, 'timeline_tweets.html', {"data": tweets_data})




# # Calculating percentage for tweet sentiments
# def percentage(part,whole):
#     return 100 * float(part) / float(whole)



