# Generated by Django 3.1.13 on 2022-01-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_checkout_email_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='due_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='email_time',
            field=models.IntegerField(blank=True),
        ),
    ]
