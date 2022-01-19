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

How to email: https://www.sitepoint.com/django-send-email/
"Less Secure App Access" in gmail settings

#### TODO:
library/views.py
library/forms.py
library/templates/email.html

Email form that can schedule when an email is sent.

https://docs.djangoproject.com/en/3.2/topics/forms/


schedule email: https://mrprabhatmishra.medium.com/periodic-email-scheduler-in-django-with-celery-beat-72c5b4d0b9d

###### You have to run this stuff for tasks to work.
Run Redis CLI `C:/Program Files/Redis/redis-cli.exe`

Celery Start Workers: https://django-celery-beat.readthedocs.io/en/latest/#example-running-periodic-tasks

```
celery -A library worker --pool=solo -l info
celery -A library beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Can't find task library.tasks.send_email
make a webscraper ---->  https://realpython.com/beautiful-soup-web-scraper-python/
site to scrape ---->  https://isbnsearch.org/isbn/ 


https://openlibrary.org/isbn/9780765326355.json

https://openlibrary.org/api/books.json?bibkeys=ISBN:9780765326355&jscmd=details&format=json

https://openlibrary.org/api/books.json?bibkeys=ISBN:9780765326355&jscmd=data&format=json

put web scraper into admin

use celery |
           |
          \ /
           '
https://www.youtube.com/watch?v=b-6mEAr1m-A

https://github.com/PrettyPrinted/youtube_video_code/tree/master/2019/09/08/Sending%20Emails%20in%20Django%20With%20Celery/django_email_celery/django_email_celery/django_email_celery  



http://127.0.0.1:8000/library/email-test/
