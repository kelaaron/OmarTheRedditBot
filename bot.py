import praw
import re
import helper

reddit = praw.Reddit('Omar')

subreddit = reddit.subreddit("cscareerquestions")

comments = subreddit.comments(limit=None)

keyphrase = "/u/omartheredditbot"

with open("/Users/aaronkelley/Documents/RedditBot/replied_comments.txt", "r") as f:
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
            #print(commlist)
            for idx in range(len(commlist)):
                #print(commlist[idx])
                if commlist[idx] == keyphrase and idx < len(commlist) - 1:
                    query = commlist[idx + 1] # make query the next word
                    break
            
            if query != "": # found a word
                late, old, count, posts = helper.search_posts(subreddit, query)
                reply = ""
                if late >= old:
                    reply = "The word \"" + query + "\" has appeared in " + str(count) + "/" + str(posts) + " posts within the last week, which is "
                    reply += str((late - old) * 100)[0:5] + "% above average. Please upvote this so I can help more!"
                    #print(reply)
                else:
                    reply = "The word \"" + query + "\" has appeared in " + str(count) + "/" + str(posts) + " posts within the last week, which is "
                    reply += str((old - late) * 100)[0:5] + "% below average. Please upvote this so I can help more!"
                    #print(reply)
                    
                try:
                    comment.reply(reply)
                    comms_replied_to.append(comment.id)
                    with open("/Users/aaronkelley/Documents/RedditBot/replied_comments.txt", "w") as f:
                        for com in comms_replied_to:
                            f.write(com + "\n")
                except:
                    pass