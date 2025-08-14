@echo off
cd /d "%~dp0"
call .venv\Scripts\activate
start uvicorn dashboard:app --host 0.0.0.0 --port 8080
python captain.py