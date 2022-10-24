import requests
import json

result = requests.get("https://www.googleapis.com/books/v1/volumes?q=uml+gota+a+gota")

book = result.json()
#print("Claves")
#print(book.keys())

items = book["items"]

encoded = json.dumps(items)
decoded = json.loads(encoded)

#Informacion del elemento n de la busqueda
#print(decoded[0])

#Informacion del volumen
#print(decoded[0]["volumeInfo"])

#Sólo el titulo
#print(decoded[0]["volumeInfo"]["title"])
#print(decoded[1]["volumeInfo"]["title"])
#print(decoded[2]["volumeInfo"]["title"])
#print(decoded[3]["volumeInfo"]["title"])
#print(decoded[4]["volumeInfo"]["title"])

#Enlace al libro
#print(decoded[0]["volumeInfo"]["infoLink"])

#print("Información del libro: ")
#print(result.status_code)
#print(result.text)