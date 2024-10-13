import requests
from datetime import datetime
import os

WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"
GENDER = "YOUR GENDER"

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
APP_ID = "YOUR APP ID"
API_KEY = "YOUR PASSWORD"
sheety_endpoint = "YOUR SHEETLY ENDPOINT"
TOKEN = "YOUR SHEETLY TOKEN"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
print(result)
for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            "exercise": exercise["name"].title(),
        },
    }

sheet_response = requests.post(
  sheety_endpoint,
  json=sheety_params,
  auth=(
      USERNAME,
      PASSWORD,
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}
sheety_response = requests.post(
    sheety_endpoint,
    json=sheety_params,
    headers=bearer_headers
)
