import requests
import json

url = "https://us-central1-pultemsoft.cloudfunctions.net/app/api/users"

payload = json.dumps({
  "name": "eeee",
  "lat": 4.6676,
  "lon": -74.5618,
  "eps": "lol"
})
headers = {
  'Content-type': 'application/json; charset=UTF-8',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())