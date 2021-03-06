# Generated by Django 3.1.13 on 2022-01-06 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20211209_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
