# Generated by Django 4.2 on 2023-05-04 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 6, 23, 49, 223413, tzinfo=datetime.timezone.utc)),
        ),
    ]