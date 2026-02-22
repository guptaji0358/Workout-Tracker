# Project - Workout Tracker
# --------------------------

import requests
from datetime import datetime

# ------------------- API CREDENTIALS -------------------

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

# ------------------- ENDPOINTS -------------------

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
Sheety_Endpoint_base_URL = "YOUR_SHEETY_ENDPOINT"

# ------------------- DATE & TIME -------------------

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

# ------------------- USER INPUT -------------------

exercise_text = input("Tell me which exercises you did: ")

# ------------------- NUTRITION API REQUEST -------------------

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_parameters = {
    "query": exercise_text
}

nutrition_response = requests.post(
    exercise_endpoint,
    json=nutrition_parameters,
    headers=nutrition_headers
)

result = nutrition_response.json()
exercises = result["exercises"]

# ------------------- SHEETY AUTH HEADER -------------------

sheety_headers = {
    "Authorization": "Bearer YOUR_BEARER_TOKEN"
}

# ------------------- PROCESS & SEND DATA -------------------

for exercise in exercises:

    total_minutes = exercise["duration_min"]

    # Duration Formatting
    if total_minutes < 60:
        formatted_duration = f"{total_minutes} Minutes"
    else:
        hours = total_minutes // 60
        remaining = total_minutes % 60

        if remaining == 0:
            formatted_duration = f"{hours:02d} Hour"
        else:
            formatted_duration = f"{hours} Hour {remaining} Minutes"

    # Build Sheety Payload
    sheety_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": formatted_duration,
            "calories": exercise["nf_calories"]
        }
    }

    # POST to Sheety
    sheety_response = requests.post(
        url=Sheety_Endpoint_base_URL,
        json=sheety_body,
        headers=sheety_headers
    )

    print(sheety_response.status_code)
    print(sheety_response.text)