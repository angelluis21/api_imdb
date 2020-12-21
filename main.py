import requests

pregunta = input("Título de la pelicula")

API_KEY="edec9890"

direccion_josep = "http://www.omdbapi.como/?apikey={}&s={}".format(API_KEY, pregunta)

requests = requests.get(direccion_josep)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos['Response'] == "False":
        print(datos["Error"])
    else:
        primera_peli = datos['Search'][0]
        clave = primera_peli['imdbID']

        otra_direccion = "http://www.omdbapi.como/?apikey={}&s={}".format(API_KEY, clave)
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos['Response'] == "False":
                print(datos["Error"])
            else:
                titulo = datos['Title']
                agno = datos['Year']
                director = datos ['Director']
                print("La peli {}, estrenada en el año {}, fue creada por {},".format(titulo,agno, director))
        else:
            print("Error por consulta id:", nueva_respuesta.status_code)
else:
    print("Error en busqueda:", respuesta.status_code)
