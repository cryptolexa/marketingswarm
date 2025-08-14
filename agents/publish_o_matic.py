import os, json, requests, schedule, time
from dotenv import load_dotenv
load_dotenv()
WP = os.getenv("WP_BASE_URL_1")
USER = os.getenv("WP_USERNAME_1")
PWD  = os.getenv("WP_APP_PASSWORD_1")

def job():
    with open("data/draft_post.txt", encoding="utf-8") as f:
        content = f.read()
    data = {"title":"AI Tools Update","content":content,"status":"publish"}
    r = requests.post(f"{WP}/wp-json/wp/v2/posts", json=data, auth=(USER,PWD))
    if r.status_code in (200,201):
        print("Publish-O-Matic: posted to WordPress")
    else:
        print("Publish-O-Matic error:", r.text)
schedule.every().day.at("09:35").do(job)
while True: schedule.run_pending(); time.sleep(60)