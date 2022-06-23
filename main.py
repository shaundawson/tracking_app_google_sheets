from keys import APP_ID, API_KEY
from http.client import responses
import requests
from datetime import datetime as dt

GENDER = 'female'
WEIGHT_KG = 72.5
HEIGHT_CM = 164.59
AGE = 39
exercise_text = "ran 3 miles"

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_parameters = {
    'query': exercise_text,
    'gender':GENDER,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':39, 
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

response = requests.post(url=nutritionix_endpoint,json=exercise_parameters,headers=headers)
data = response.json()
print(data)