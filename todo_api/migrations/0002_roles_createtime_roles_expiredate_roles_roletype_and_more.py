# Generated by Django 4.0.5 on 2022-06-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='createTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='roles',
            name='expireDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='roles',
            name='roleType',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='roles',
            name='userID',
            field=models.IntegerField(null=True),
        ),
    ]
