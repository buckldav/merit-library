# Generated by Django 3.1.13 on 2021-12-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic=False

    dependencies = [
        ('library', '0003_auto_20211203_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='dewey_decimal',
            new_name='call_number',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='barcode',
            new_name='isbn',
        ),
        migrations.AlterField(
            model_name='book',
            name='copies',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
