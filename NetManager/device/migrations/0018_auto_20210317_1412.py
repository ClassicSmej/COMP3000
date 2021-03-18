# Generated by Django 3.1.5 on 2021-03-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0017_auto_20210309_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='device',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
