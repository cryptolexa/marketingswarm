import json, ollama, schedule, time
def job():
    with open("data/draft_post.txt", encoding="utf-8") as f:
        post = f.read()
    prompt = f"Turn this blog post into a 60-second TikTok script:\n{post}"
    res = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])
    with open("data/tiktok_script.txt","w", encoding="utf-8") as f:
        f.write(res["message"]["content"])
    print("Repurpose-Bot: saved TikTok script")
schedule.every().day.at("09:45").do(job)
while True: schedule.run_pending(); time.sleep(60)