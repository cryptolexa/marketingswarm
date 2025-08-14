import os, time, json, datetime
def log(msg):
    with open("data/logs.txt","a") as f:
        f.write(f"{datetime.datetime.now()} {msg}\n")
while True:
    for a in os.listdir("agents"):
        if a.endswith(".py"):
            log(f"{a} heartbeat")
    time.sleep(3600)