import praw

reddit = praw.Reddit('Omar')

subreddit = reddit.subreddit("cscareerquestions")

for post in subreddit.hot(limit = 5):
    print("Title= ", post.title)
    print("text= ", post.selftext)
    print("score= ", post.score)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")