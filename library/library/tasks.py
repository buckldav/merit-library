from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task
from time import sleep

@shared_task
def wait(duration):
    sleep(duration)
    return None

def send_email():
    wait(300)
    send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, ["bryson.day@meritknights.com"], fail_silently=False)
    return None