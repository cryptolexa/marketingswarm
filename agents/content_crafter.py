import ollama, json, schedule, time, os
from dotenv import load_dotenv

load_dotenv()

def job():
    with open("data/hot_topics.json") as f:
        topic = json.load(f)["trends"][0]["keyword"]
    prompt = f"Write a 200-word blog post intro about '{topic}'."
    try:
        res = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])
        post = res["message"]["content"]
        with open("data/draft_post.txt","w",encoding="utf-8") as f:
            f.write(post)
        print("Content-Crafter: draft_post.txt saved")
    except Exception as e:
        print("Content-Crafter error:", e)

schedule.every().day.at("09:15").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)