import requests
import json

url = "https://swapi.dev/api/people/4"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("response.json", "a", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
else:
    print("Error:", response.status_code)
