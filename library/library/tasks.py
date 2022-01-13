from django.conf import settings
from django.core.mail import send_mail
from library.library.models import Checkout
# from celery import shared_task
from celery.contrib.abortable import AbortableTask
from config.settings.celery import app
from time import sleep

@app.task(bind=True, base=AbortableTask)
def send_overdue_email(self, checkout):
    #duration = Checkout.due_date_time - checkout_time
    sleep((checkout.due_date - checkout.checkout_time).total_seconds())
    # try to get checkout object from db if exists
    try:
        # if not self.is_aborted():
            print("email!")
            checkout = Checkout.objects.get(id=checkout.id)
            recipient = checkout.student.email #recipient = student email 
            send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    except:
        # the book was checked in
        pass


# def send_email():
#     wait(300)
#     send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, ["bryson.day@meritknights.com"], fail_silently=False)
#     return None