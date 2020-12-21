import requests

direccion = "http://www.omdbapi.com/?apikey=edec9890&i=tt3896198" # url a la que quiero llamar

# hacer petición http
respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()
    print(datos)
else:
    print("Se ha producido un error", respuesta.status_code)
