from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:question_id>/',views.index,name='Twitter_Analysis'),
    #############################     CSK URLs    #####################################
    path('get_CSK_timeline_tweets/',views.get_CSK_timeline_tweets,name='Twitter_Analysis'),
    path('top_ten_CSK_tweets/',views.top_ten_CSK_tweets,name='Top Ten  CSK Tweets'),
    path('top_ten_CSK_tweets_graph/',views.top_ten_CSK_tweets_graph,name='Top Ten  CSK Tweets'),
    #############################     RCB URLs    #####################################
    path('get_RCB_timeline_tweets/',views.get_RCB_timeline_tweets,name='Twitter_Analysis'),
    path('top_ten_RCB_tweets/',views.top_ten_RCB_tweets,name='Top Ten  RCB Tweets'),
    path('top_ten_RCB_tweets_graph/',views.top_ten_RCB_tweets_graph,name='Top Ten  RCB Tweets'),
    #############################     KKR URLs    #####################################
    path('get_KKR_timeline_tweets/',views.get_KKR_timeline_tweets,name='Twitter_Analysis'),
    path('top_ten_KKR_tweets/',views.top_ten_KKR_tweets,name='Top Ten  KKR Tweets'),
    path('top_ten_KKR_tweets_graph/',views.top_ten_KKR_tweets_graph,name='Top Ten  KKR Tweets'),
    ############################     MI URLs     #####################################
    path('get_MI_timeline_tweets/',views.get_MI_timeline_tweets,name='Twitter_Analysis'),
    path('top_ten_MI_tweets/',views.top_ten_MI_tweets,name='Top Ten  MI Tweets'),
    path('top_ten_MI_tweets_graph/',views.top_ten_MI_tweets_graph,name='Top Ten  MI Tweets'),

]