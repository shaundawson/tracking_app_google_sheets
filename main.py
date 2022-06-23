from keys import NTX_APP_ID, NTX_API_KEY, SHEETY_USERNAME, SHEETY_PROJECT, SHEETY_SHEETNAME,BEARER
from http.client import responses
import requests
from datetime import datetime as dt

GENDER = 'female'
WEIGHT_KG = 72.5
HEIGHT_CM = 164.59
AGE = 39

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEETY_SHEETNAME}'

exercise_text = input("Tell me which exercises you did: ")

ntx_headers = {
    'x-app-id': NTX_APP_ID,
    'x-app-key': NTX_API_KEY,
}

exercise_parameters = {
    'query': exercise_text,
    'gender':GENDER,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':39, 
}

response = requests.post(url=nutritionix_endpoint,json=exercise_parameters,headers=ntx_headers)
result = response.json()
# print(result)


today= dt.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

sheet_headers = {
    'Authorization': BEARER
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


# #POST
sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=sheet_headers)
print(sheet_response.text)




