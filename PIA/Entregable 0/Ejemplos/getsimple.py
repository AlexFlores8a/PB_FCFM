import requests

url = "https://swapi.dev/api/people/4"
response = requests.get(url)

print("Status code:", response.status_code)
print("Tipo de dato:", type(response.json()))
