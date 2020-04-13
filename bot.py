import praw
import re

reddit = praw.Reddit('Omar')

subreddit = reddit.subreddit("cscareerquestions")

for post in subreddit.hot(limit = 5):

    if(re.search())
    print("Title= ", post.title)
    print("text= ", post.selftext)
    print("score= ", post.score)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")