# Generated by Django 4.0.5 on 2022-06-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0003_persions'),
    ]

    operations = [
        migrations.AddField(
            model_name='persions',
            name='managerID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
