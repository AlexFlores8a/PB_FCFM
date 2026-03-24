import requests

url = "https://swapi.dev/api/people/a"
response = requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print("Falló, Status code:", response.status_code)
