# Generated by Django 3.1.13 on 2022-01-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20220106_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='email_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
