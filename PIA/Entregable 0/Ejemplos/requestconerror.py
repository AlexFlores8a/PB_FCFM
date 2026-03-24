import requests

url = "https://swapi.dev/api/people/a"
response = requests.get(url)

print("Status code:", response.status_code)
