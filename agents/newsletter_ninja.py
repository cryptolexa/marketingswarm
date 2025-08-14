import json, requests, schedule, time
def job():
    with open("data/draft_post.txt", encoding="utf-8") as f:
        summary = f.read()[:500]
    # Placeholder Mailchimp call
    print("Newsletter-Ninja: would send summary via Mailchimp")
schedule.every().sunday.at("09:00").do(job)
while True: schedule.run_pending(); time.sleep(60)