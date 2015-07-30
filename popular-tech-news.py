#author: https://github.com/anandaverma
#Gives url which is trending both in hackernews and reddit. Some more logic and we can detect viral news on internet
#HackerNews top posts
import urllib2
import json
baseUrl = 'https://hacker-news.firebaseio.com/v0/item/{0}.json?print=pretty'
response = urllib2.urlopen('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
topIds = json.load(response)
urls = []
for index in range(50):
        #print index
        url = baseUrl.format(topIds[index])
        #print(url)
        popular = urllib2.urlopen(url)
        HN = json.load(popular)
        #print(HN)
        if('url' in HN.keys()):
                urls.append(HN['url'].strip("/"))
#print(urls)

#reddit to post in technology
import time
import praw
from pprint import pprint
r = praw.Reddit(user_agent='fossbytes')
#replace username and password
r.login('techy221','Bril4359#')
subreddit = r.get_subreddit('technology')
topPosts = []
for submission in subreddit.get_hot(limit=50):
        # Test if it contains a PRAW-related question
        topPosts.append(submission.url.strip("/"))
#print(topPosts)

print('popular in both')
common = list(set(urls) & set(topPosts))
for item in common:
        print(item)