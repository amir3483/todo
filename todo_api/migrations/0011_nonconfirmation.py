# Generated by Django 4.0.5 on 2022-07-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0010_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.TextField(blank=True, verbose_name='علت عدم تایید')),
            ],
        ),
    ]
