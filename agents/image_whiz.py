import os, requests, json, schedule, time
def job():
    with open("data/outlines.json") as f:
        topic = json.loads(f.read())[0]["title"]
    url = "http://localhost:11434/api/generate"
    payload = {"model":"llama3.1:8b","prompt":f"Short one-line prompt for Stable Diffusion image about '{topic}'","stream":False}
    r = requests.post(url, json=payload)
    prompt2 = r.json()["response"]
    # Save prompt for Stable Diffusion UI to pick up later
    with open("data/image_prompt.txt","w") as f: f.write(prompt2)
    print("Image-Whiz: created prompt")
schedule.every().day.at("09:20").do(job)
while True: schedule.run_pending(); time.sleep(60)