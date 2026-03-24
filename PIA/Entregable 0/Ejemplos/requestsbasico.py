import requests

response = requests.get("https://swapi.dev/api/people/4")
print(response.status_code)
data = response.json()
print(type(data))  # dict
for x,y in data.items():
    print(x,y)
