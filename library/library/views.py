from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import EmailForm
from celery import shared_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from .tasks import wait

# schedule, _ = CrontabSchedule.objects.get_or_create(
#     minute='1',
#     hour='*',
#     day_of_week='*',
#     day_of_month='*',
#     month_of_year='*',
# )

# PeriodicTask.objects.create(
#     crontab=schedule,
#     name='Send Lots Of Emails!',
#     task='library.library.tasks.send_email',
# )
# Create your views here.



def email_scheduler(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            wait(30)
            recipient = form.data["your_email"]
            send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            # ...
            # redirect to a new URL:
            return render(request, 'email.html')
        else:
            return render(request, 'email.html', status=400)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'email.html', {'form': form})
