import os, time, subprocess, schedule, json
from dotenv import load_dotenv

load_dotenv()
AGENTS = [
    "trend_spotter.py",
    "outline_forge.py",
    "content_crafter.py",
    "image_whiz.py",
    "publish_o_matic.py",
    "seo_tuner.py",
    "social_scheduler.py",
    "backlink_buddy.py",
    "analytics_scribe.py",
    "repurpose_bot.py",
    "newsletter_ninja.py"
]

def run(agent):
    subprocess.Popen(["python", agent], cwd=os.getcwd())

if __name__ == "__main__":
    for a in AGENTS:
        run(a)
    while True:
        time.sleep(60)