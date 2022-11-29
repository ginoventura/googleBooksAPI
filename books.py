import requests
import json

# 1) Libros de un tema especifico, sin filtros
#result = requests.get("https://www.googleapis.com/books/v1/volumes?q=java")

# 2) Libros disponibles electronicamente
result = requests.get("https://www.googleapis.com/books/v1/volumes?q=html&download=epub")

# 3) Libros gratis y disponibles electronicamente
#result = requests.get("https://www.googleapis.com/books/v1/volumes?q=bases+de+datos&filter=free-ebooks&download=epub")

book = result.json()
#print("Claves")
#print(book.keys())

items = book["items"]

encoded = json.dumps(items)
decoded = json.loads(encoded)

# ----------------------------------------------
#print(decoded[0]["volumeInfo"]["title"])
#print(decoded[0]["volumeInfo"]["infoLink"])
#print("")

#print(decoded[1]["volumeInfo"]["title"])
#print(decoded[1]["volumeInfo"]["infoLink"])
#print("")

#print(decoded[2]["volumeInfo"]["title"])
#print(decoded[2]["volumeInfo"]["infoLink"])
#print("")

#print(decoded[3]["volumeInfo"]["title"])
#print(decoded[3]["volumeInfo"]["infoLink"])
#print("")
# ---------------------------------------------

#print(decoded[4]["volumeInfo"]["title"])
#print(decoded[4]["volumeInfo"]["infoLink"])
#print("")

#print(decoded[5]["volumeInfo"]["title"])
#print(decoded[5]["volumeInfo"]["infoLink"])
#print("")

#Informacion
print(decoded[0])
#print(decoded[1]["volumeInfo"]["publishedDate"])
#print(decoded[2]["volumeInfo"]["publishedDate"])
#print(decoded[3]["volumeInfo"]["publishedDate"])

#Enlace al libro
#print(decoded[0]["volumeInfo"]["infoLink"])

#print("Información del libro: ")
#print(result.status_code)
#print(result.text)