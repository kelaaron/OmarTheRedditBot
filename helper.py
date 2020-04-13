import praw
import re
import datetime

def search_posts(subreddit, query):
    lately_count = 0
    old_count = 0
    lately_posts = 0
    old_posts = 0
    now = datetime.datetime.utcnow()
    #now = float(now.strftime("%s"))
    print(now)
    # now = (now - datetime(1970,1,1, tzinfo=timezone.utc)) / timedelta(seconds=1)
    for submission in subreddit.new(limit=None):
        # print(submission.created_utc)
        # print(submission.title)
        # print(submission.selftext)
        if(now - datetime.timedelta(days=30) <= datetime.datetime.fromtimestamp(submission.created_utc)):
            lately_posts += 1
            if re.search(query, submission.title, re.IGNORECASE):
                lately_count += 1
            elif re.search(query, submission.selftext, re.IGNORECASE):
                lately_count += 1
        else:
            old_posts += 1
            if re.search(query, submission.title, re.IGNORECASE):
                old_count += 1
            elif re.search(query, submission.selftext, re.IGNORECASE):
                old_count += 1
    return lately_count / lately_posts, old_count / old_posts, lately_count, lately_posts
    