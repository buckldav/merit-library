### Commands

#### Project Setup

```bash
python -m venv env
source env/Scripts/activate
pip install django
django-admin startproject <project-name> .
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