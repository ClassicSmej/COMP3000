# Generated by Django 3.1.5 on 2021-03-28 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0031_auto_20210326_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 18, 23, 14, 746694)),
        ),
    ]
