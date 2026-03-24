import requests
import json

##Hacemos un request para obtener el reporte actual
## Ver documentacion para su uso https://openweathermap.org/api/one-call-api
#Definimos las variables para hacer la petición
lat = "28.5421109"
lon = "-81.3790304"
appid = "4a48cd05b67e129b902f78dd829318b1"#sustituir por tu API id
page = requests.get ("https://api.openweathermap.org/data/"+
                     "3.0/onecall?lat="+lat+"&lon="+lon
                     +"&exclude=minutely,hourly,daily"
                     +"&units=metric&appid="+appid)
                    #Internamente es un método HTTP GET
print (page.status_code) #Status code 200 significa "Ok", 
print ("Page es de tipo:",type(page))
print ("Page content es de tipo:",type(page.content))

input ("Vamos a imprimir el contenido de la página")
print (page.content)
input("parse del contenido de la página a json")
weatherData = json.loads(page.content)
print ("El tipo de dato ahora es:", type(weatherData))
input("Vamos a imprimir el dict")
for x,y in weatherData.items():
    print(x+":",y)


input("las keys del dictionary")
for key in weatherData:
    print (key,":",type(weatherData[key]))
print ("current es de tipo diccionario")

input("Imprimimos el diccionario current")
for elem in weatherData["current"]:
    print (elem,":\t",weatherData["current"][elem])

input ("Como weather es un dict, imprimimos sus valores")
for key in weatherData["current"]["weather"][0]:
    print (key,"\t",weatherData["current"]["weather"][0][key], "\t",type(key))
