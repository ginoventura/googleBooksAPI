import web
import requests 
import json

render = web.template.render("mvc/")

class Index():
  def GET(self):
    datos = None
    return render.index(datos)

  def POST(self):
    form = web.input()
    book_name = form.book_name

  # Libros por nombre
    #result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)
  
  # Libros disponibles electronicamente    
    #result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name+"&download=epub")

  # Libros gratuitos y disponibles electronicamente
    result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name+"&filter=free-ebooks&download=epub")

    book = result.json()
    items = book["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    books = []

    for book in decoded:
      url = book["volumeInfo"]["infoLink"]
      titulo = book["volumeInfo"]["title"]
      #fechaPublicacion = book["volumeInfo"]["publishedDate"]

      datos = {
        "book_name":book_name,
        "titulo":titulo,
        #"fechaPublicacion":fechaPublicacion,
        "url":url
      }
      books.append(datos)

    print(books)

    return render.index(books)