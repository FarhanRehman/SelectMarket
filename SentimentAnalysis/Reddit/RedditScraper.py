# Import Libraries
from Database.db import DatabaseManager
from config import config
import praw

# 1) Getting the data - in this case, we'll be scraping data from a reddit with PRAW

class RedditScraper:
    def __init__(self, subreddit):
        # Initialize Variables
        self.subreddit = subreddit

        # Set up Reddit Scraper using credentials
        self.reddit = praw.Reddit(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            user_agent=config.USER_AGENT
        )

        # Use this to increment statistics (Comments count, Mentions count, Positions count)
        DB = DatabaseManager()
        DB.incrementStatistics("COMMENTS")

    # filter by search/flair
    def searchSubreddit(self, query, sort, syntax, timeFilter):
        for submission in reddit.subreddit(self.subreddit).search(query, sort=sort, syntax=syntax, time_filter=timeFilter ):
            return submission

    # Stream Daily/Weekend Discussion
    def wsbDiscussion(self):
        return self.reddit.subreddit(self.subreddit).sticky()


    # The tool scrapes WallStreetBets "hot" topics and scans for any tickers mentioned in the topic title. If a ticker or company name (ie: Amazon for $AMZN) is found, it continues to scan the comments of said topic.
    
    def streamSubmissions(self):
        for submission in self.reddit.subreddit(self.subreddit).stream.submissions():
            return submission

    def streamComments(self):
        for comment in self.reddit.subreddit(self.subreddit).stream.comments():
            return comment
        
    # Get submissions based on sort and time filter
    def topSubmissions(self, time_filter):   
        submissions = []

        for submission in self.subreddit(SUBREDDIT).top(time_filter=time_filter, limit=250):
            submissions.append(submission)
        
        return submissions

    def hotSubmissions(self, time_filter):   
        submissions = []
        
        for submission in self.reddit.subreddit(SUBREDDIT).hot(time_filter=time_filter, limit=250):
            submissions.append(submission)
        
        return submissions

    def newSubmissions(self, time_filter):   
        submissions = []
        
        for submission in self.reddit.subreddit(SUBREDDIT).new(time_filter=time_filter, limit=250):
            submissions.append(submission)
        
        return submissions

    def controversialSubmissions(self, time_filter):   
        submissions = []
        
        for submission in self.reddit.subreddit(SUBREDDIT).controversial(time_filter=time_filter, limit=250):
            submissions.append(submission)
        
        return submissions

    def risingSubmissions(self, time_filter):   
        submissions = []
        
        for submission in self.reddit.subreddit(SUBREDDIT).rising(time_filter=time_filter, limit=250):
            submissions.append(submission)
        
        return submissions

    # Get comments based on sort
    def getComments(self, id, sort):
        submission = self.reddit.submission(id=id)
        commentsList = []

        # set sort category
        submission.comment_sort = sort

        # make comment limit to ~25% of total comments
        submission.comment_limit = round(submission.num_comments * 0.25)

        submission.comments.replace_more(limit=None, threshold=0)
        for comment in submission.comments:
            commentsList.append(f"{counter}) {comment.body} | {comment.points}")
        
        return commentsList

