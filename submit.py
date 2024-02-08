import requests
import json

url = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge'
body = {
    "github": "https://github.com/RidaIftikhar14/DPS-Challenge-2023-.git",
    "email": "ridaiftikhar430@gmail.com",
    "url": "https://dps-app-09bb6ce17a11.herokuapp.com/",
    "notes": " "  # This field is optional
}

headers = {
    'Content-Type': 'application/json'
}

POST request
response = requests.post(url, json=body, headers=headers)

# Get the status code and the response JSON
status_code = response.status_code
response_json = response.json()

print(status_code, response_json)
