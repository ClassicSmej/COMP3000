# Generated by Django 3.1.5 on 2021-03-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0012_auto_20210216_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=250)),
                ('user', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('dateTime', models.CharField(max_length=250)),
            ],
        ),
    ]