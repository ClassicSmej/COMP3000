# Generated by Django 3.1.5 on 2021-04-06 22:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('host', models.CharField(max_length=250)),
                ('vendor', models.CharField(max_length=250)),
                ('location', models.CharField(default='Not Specified', max_length=250)),
                ('contact', models.CharField(default='Not Specified', max_length=250)),
                ('status', models.BooleanField(default=False, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('secret', models.CharField(blank=True, max_length=250, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('device', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateField(default=datetime.date(2021, 4, 6))),
                ('time', models.TimeField(default=datetime.time(22, 36, 40, 686451))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]