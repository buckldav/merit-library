from django.urls import path
from library.library.views import email_scheduler

urlpatterns = [
    path("email-test/", email_scheduler, name="email-test"),

]
