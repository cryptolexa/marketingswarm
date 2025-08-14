import requests, schedule, time, json, os
from datetime import datetime

def job():
    url = "https://trends.googleapis.com/trends/api/explore"
    params = {"hl":"en-US","tz":-120,"req":json.dumps({"comparisonItem":[{"keyword":"AI tools","geo":"","time":"today 12-m"}],"category":0,"property":""})}
    try:
        r = requests.get(url, params=params)
        data = r.text[5:]  # strip leading junk
        trends = json.loads(data)
        with open("data/hot_topics.json","w") as f:
            json.dump({"date":str(datetime.now()),"trends":trends},f)
        print("Trend-Spotter: updated hot_topics.json")
    except Exception as e:
        print("Trend-Spotter error:", e)

os.makedirs("data", exist_ok=True)
schedule.every().day.at("09:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)