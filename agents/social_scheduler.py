import tweepy, praw, json, os, schedule, time
from dotenv import load_dotenv

load_dotenv()

# Twitter
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET")
)
twitter = tweepy.API(auth)

# Reddit
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="MarketingSwarm/1.0"
)

def job():
    with open("data/draft_post.txt", encoding="utf-8") as f:
        text = f.read()[:280]
    try:
        twitter.update_status(text)
        reddit.subreddit("test").submit(title="AI Tools Update", selftext=text)
        print("Social-Scheduler posted")
    except Exception as e:
        print("Social-Scheduler error:", e)

schedule.every().day.at("09:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)