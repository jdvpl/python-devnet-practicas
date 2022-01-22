import requests
import json

url = "https://us-central1-pultemsoft.cloudfunctions.net/app/api/users"

payload = json.dumps({
  "name": "Jiren",
  "lat": 4.6676,
  "lon": -74.5618,
  "eps": "lol"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data="hola")

print(response.text)