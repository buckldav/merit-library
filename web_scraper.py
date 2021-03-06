import requests
import json
import pprint
from stdnum.isbn import to_isbn10

# Open library likes isbn 10's
ISBN = "9780590353427"
if len(ISBN) == 13:
    ISBN = ISBN[0:3] + "-" + ISBN[3:]
    ISBN = to_isbn10(ISBN).strip("-")

# Get title and picture
#URL = "https://isbndb.com/book/9780765378484"
URL = f"https://openlibrary.org/api/books.json?jscmd=data&bibkeys=ISBN:{ISBN}"
page = requests.get(URL)
data = json.loads(page.content.decode("utf-8"))

#URL_2 = f"https://openlibrary.org/api/books.json?bibkeys=ISBN:{ISBN}&jscmd=data&format=json"
#page = requests.get(URL_2)
#data = json.loads(page.content.decode("utf-8"))

#AUTHOR_URL = f"https://openlibrary.org{data['authors'][0]['key']}.json"
#page = requests.get(AUTHOR_URL)
#author_data = json.loads(page.content.decode("utf-8"))

book = {
    "title": data[f"ISBN:{ISBN}"]["title"],
    "cover": data[f"ISBN:{ISBN}"]["cover"]["medium"],
    "pages": data[f"ISBN:{ISBN}"]["number_of_pages"],
    "barcode": ISBN,

    "author": {
        "first_name": " ".join(data[f"ISBN:{ISBN}"]["authors"][0]["name"].split()[0:-1]),
        "last_name": data[f"ISBN:{ISBN}"]["authors"][0]["name"].split()[-1]
    }
}

print(book)
