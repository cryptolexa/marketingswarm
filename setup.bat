@echo off
echo === Marketing-Swarm Setup ===
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
echo.
echo All done!  Copy your keys into .env then run start.bat
pause