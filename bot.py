import praw
import re
import helper

reddit = praw.Reddit('Omar')

subreddit = reddit.subreddit("testingground4bots")

comments = subreddit.comments(limit=None)

keyphrase = "/u/omartheredditbot"

with open("replied_comments.txt", "r") as f:
    comms_replied_to = f.read()
    comms_replied_to = comms_replied_to.split("\n")
    comms_replied_to = list(filter(None, comms_replied_to)) # creates a list of comments

for comment in comments:
    #print(comment.body.lower())

    if keyphrase in comment.body.lower(): # Check if someone tags Omar
        print(comment.body.lower())
        print(type(comment.body.lower()))

        if comment.id not in comms_replied_to:

            query = ""
            commlist = comment.body.lower().split()
            print(commlist)
            for idx in range(len(commlist)):
                print(commlist[idx])
                if commlist[idx] == keyphrase and idx < len(commlist) - 1:
                    query = commlist[idx + 1] # make query the next word
                    print("QUERY = ", query)
                    break
            
            if query != "": # found a word
                late, old = helper.search_posts(subreddit, query)
                print("FOUND WORD ", query, "WITH VALUES ", late, ", ", old)






    