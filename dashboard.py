from fastapi import FastAPI, FileResponse
import os, json

app = FastAPI()

@app.get("/")
def home():
    status = {}
    for f in os.listdir("data"):
        if f.endswith(".json"):
            with open(os.path.join("data", f)) as fp:
                status[f] = "✅" if fp.read() else "❌"
    return {"agents_status": status, "dashboard":"http://localhost:8080"}

@app.get("/logs")
def logs():
    return FileResponse("data/logs.txt") if os.path.exists("data/logs.txt") else {"logs":"no logs yet"}