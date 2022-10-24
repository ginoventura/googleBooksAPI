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

    result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)

    book = result.json()
    items = book["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    books = []

    for book in decoded:
      url = book["volumeInfo"]["infoLink"]
      titulo = book["volumeInfo"]["title"]

      datos = {
        "book_name":book_name,
        "titulo":titulo,
        "url":url
      }
      books.append(datos)

    print(books)

    return render.index(books)