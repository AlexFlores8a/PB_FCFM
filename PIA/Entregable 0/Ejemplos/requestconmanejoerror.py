import requests

url = "https://swapi.dev/api/people/4"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Conexión exitosa")
    else:
        print("Error en la API:", response.status_code)
except Exception as e:
    print("Error de conexión:", e)
