from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_email():
    send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, ["bryson.day@meritknights.com"], fail_silently=False)
    return None