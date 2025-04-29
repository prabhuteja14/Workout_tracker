import json
import requests
from datetime import datetime

# === CONFIG ===
BOT_TOKEN = "7948211582:AAEbQnVCM-blb6sz9ZuNTnuyxmN98M61PN"
CHAT_ID = "1051856867"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

# === MAIN CHECK ===
with open("workout_log.json") as f:
    data = json.load(f)

last_workout_str = data.get("last_workout")
last_workout_date = datetime.strptime(last_workout_str, "%Y-%m-%d")
today = datetime.today()

days_since = (today - last_workout_date).days

if days_since >= 2:
    alert = f"🚨 It’s been {days_since} days since your last workout! Time to move 💪"
    print(alert)
    send_telegram_alert(alert)
else:
    print(f"✅ You're on track! Last workout was {days_since} day(s) ago.")

