# Generated by Django 4.0.5 on 2022-08-25 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0021_rename_month_form1_month_rename_region_form1_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonconfirmation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='تاریخ'),
        ),
        migrations.AddField(
            model_name='nonconfirmation',
            name='form',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='شماره فرم'),
        ),
    ]
