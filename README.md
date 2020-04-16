# Reddit Statistical Analysis Bot
This is a bot built for Reddit. It enables users to track usage data for query words on a specific subreddit.
It uses [Reddit API](https://www.reddit.com/dev/api/) and [Praw](https://praw.readthedocs.io/en/latest/) to create a simple bot to analyze the usage of query words.
## How it works
When tagged in a post comment on a respective subreddit and given a query word immediately following the tag, Omar will parse the subreddit and count instances of posts which include that word. Then, it will separate usage by time, and report the frequency trend of the query word on the respective subreddit.
## Usage
To summon Omar, simply write a comment that includes /u/OmarTheRedditBot <query>, and the bot will run analytics on that query word.
** Note: As of now, Omar will only work on the r/testingground4bots until development is completed. This is to prevent unnecessary banning of its user agent.
