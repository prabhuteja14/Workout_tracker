import json
from datetime import date

today = date.today().isoformat()

data = {
    "last_workout": today
}

with open("workout_log.json", "w") as f:
    json.dump(data, f)

print(f"✅ Workout logged for today: {today}")

