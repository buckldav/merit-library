### Commands

#### Project Setup

```bash
python -m venv env
source env/Scripts/activate
pip install -r requirements/local.txt
```
#### run server
```bash
source env/Scripts/activate

python manage.py runserver
```

#### Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

#### make an app
```bash
django-admin startapp <app-name>
```

#### migration

```bash
python manage.py makemigrations
python manage.py migrate
```

make a webscraper ---->  https://realpython.com/beautiful-soup-web-scraper-python/
site to scrape ---->  https://isbnsearch.org/isbn/ 


https://openlibrary.org/isbn/9780765326355.json

https://openlibrary.org/api/books.json?bibkeys=ISBN:9780765326355&jscmd=details&format=json

https://openlibrary.org/api/books.json?bibkeys=ISBN:9780765326355&jscmd=data&format=json

put web scraper into admin