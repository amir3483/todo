# Generated by Django 4.0.5 on 2022-06-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0007_location_stations_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='form1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.CharField(blank=True, max_length=50)),
                ('Region', models.CharField(blank=True, max_length=200)),
                ('StationName', models.CharField(blank=True, max_length=200)),
                ('Row1', models.TextField(blank=True, verbose_name='قفل بودن درب محوطه ایستگاه')),
                ('Row2', models.TextField(blank=True, verbose_name='قفل بودن درب جعبه تجهیزات')),
                ('Row3', models.TextField(blank=True, verbose_name='عدم وجود آب، برف، علوفه، زباله، نخاله و... در محوطه ایستگاه و اطراف')),
                ('Row4', models.TextField(blank=True, verbose_name='عدم گسترش پوشش گیاهی موجود (درختان و ..). در محوطه و اطراف ایستگاه')),
                ('Row5', models.TextField(blank=True, verbose_name='عدم انجام عملیات عمرانی در محوطه ایستگاه و اطراف')),
                ('Row6', models.TextField(blank=True, verbose_name='عدم وجود هرگونه مانع و تجهیزات در مجاورت ایستگاه تا فاصله  2متری')),
                ('Row7', models.TextField(blank=True, verbose_name='کنترل وضعیت برق ایستگاه')),
                ('Row8', models.TextField(blank=True, verbose_name='وضعیت سیستمهای ارتباطی و آنتن خارجی')),
                ('Row9', models.TextField(blank=True, verbose_name='تعداد و تاریخ مراجعه اضطراری به ایستگاه')),
                ('Row10', models.TextField(blank=True, verbose_name='سایر موارد - موارد اعلامی از سوی سازمان')),
                ('ReportDate', models.DateTimeField(null=True, verbose_name='تاریخ تهیه گزارش')),
                ('Responsible1Name', models.CharField(blank=True, max_length=200, verbose_name='نام مسئول تهیه گزارش')),
                ('Responsible1Signature', models.ImageField(upload_to='images/', verbose_name='امضاء مسئول تهیه گزارش')),
                ('Responsible2Name', models.CharField(blank=True, max_length=200, verbose_name='نام مسئول تایید گزارش')),
                ('Responsible2Signature', models.ImageField(upload_to='images/', verbose_name='امضاء مسئول تایید گزارش')),
            ],
        ),
    ]
