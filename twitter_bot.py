from tkinter import *
import tweepy
import twitter_credentials
import random

# set up application
window = Tk()
window.title('Twitter Bot')
window.geometry("600x400")

# import tokens
ACCESS_TOKEN = twitter_credentials.ACCESS_TOKEN
ACCESS_SECRET = twitter_credentials.ACCESS_SECRET
CONSUMER_KEY = twitter_credentials.CONSUMER_KEY
CONSUMER_SECRET = twitter_credentials.CONSUMER_SECRET

# authorize Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

title = Label(window, text = 'Twitter Bot')
title.pack()

# post directly to twitter
def post():
    api.update_status(to_post.get())

to_post = Entry(window, width = 30)
to_post.pack()

post_button = Button(window, text = 'Post to Twitter', command = post)
post_button.pack()

# search for all tweets from a certain date using hashtags
def search_general():
    if number_entry.get() == '':
        tweets = tweepy.Cursor(api.search, q = search_words, lang = "en", since = date_since).items()
    else:
        tweets = tweepy.Cursor(api.search, q = search_words, lang = "en", since = date_since).items(int(number_entry.get()))
    for tweet in tweets:
        print(tweet.text)

# get keywords
keywords = Label(window, text = 'Enter hashtags separated by a space')
keywords.pack()
key_entry = Entry(window, width = 30)
key_entry.pack()
search_words = key_entry.get().split()

# get starting search date
date = Label(window, text = 'Enter the start date of your search in the form YYYY-MM-DD')
date.pack()
date_entry = Entry(window, width = 30)
date_entry.pack()
date_since = date_entry.get()

# get maximum number of tweets to display
number_label = Label(window, text = 'Enter the maximum number of tweets to display. Leave blank if no maximum.')
number_label.pack()
number_entry = Entry(window, width = 30)
number_entry.pack()

search_button = Button(window, text = 'Search by hashtag', command = search_general)
search_button.pack()

# run application
window.mainloop()
'''public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)'''

'''user = api.get_user('twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)'''

'''class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

streamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = streamListener)
tweeter = myStream.filter(track='python')

for tweet in tweeter:
    #-----------------------------------------------------------------------
    # print out the contents, and any URLs found inside
    #-----------------------------------------------------------------------
    for url in tweet["entities"]["urls"]:
        print(" - found URL: %s" % url["expanded_url"])'''