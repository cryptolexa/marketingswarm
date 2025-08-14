import json, ollama, schedule, time, os
def job():
    with open("data/hot_topics.json") as f:
        kw = json.load(f)["trends"][0]["keyword"]
    prompt = f"Write 3 SEO blog post outlines for '{kw}' in JSON [{kw}]."
    res = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])
    with open("data/outlines.json","w",encoding="utf-8") as f:
        f.write(res["message"]["content"])
    print("Outline-Forge: saved outlines.json")
schedule.every().day.at("09:05").do(job)
while True: schedule.run_pending(); time.sleep(60)