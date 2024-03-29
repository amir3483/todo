# Generated by Django 4.0.5 on 2022-08-25 21:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_api', '0022_nonconfirmation_date_nonconfirmation_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('station_name', models.CharField(blank=True, max_length=200, null=True)),
                ('row1', models.TextField(blank=True, null=True, verbose_name='قفل بودن درب محوطه ایستگاه')),
                ('row2', models.TextField(blank=True, null=True, verbose_name='قفل بودن درب جعبه تجهیزات')),
                ('row3', models.TextField(blank=True, null=True, verbose_name='عدم وجود آب، برف، علوفه، زباله، نخاله و... در محوطه ایستگاه و اطراف')),
                ('row4', models.TextField(blank=True, null=True, verbose_name='عدم گسترش پوشش گیاهی موجود (درختان و ..). در محوطه و اطراف ایستگاه')),
                ('row5', models.TextField(blank=True, null=True, verbose_name='عدم انجام عملیات عمرانی در محوطه ایستگاه و اطراف')),
                ('row6', models.TextField(blank=True, null=True, verbose_name='عدم وجود هرگونه مانع و تجهیزات در مجاورت ایستگاه تا فاصله  2متری')),
                ('row7', models.TextField(blank=True, null=True, verbose_name='کنترل وضعیت برق ایستگاه')),
                ('row8', models.TextField(blank=True, null=True, verbose_name='وضعیت سیستمهای ارتباطی و آنتن خارجی')),
                ('row9', models.TextField(blank=True, null=True, verbose_name='تعداد و تاریخ مراجعه اضطراری به ایستگاه')),
                ('row10', models.TextField(blank=True, null=True, verbose_name='سایر موارد - موارد اعلامی از سوی سازمان')),
                ('report_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='تاریخ تهیه گزارش')),
                ('responsible1_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مسئول تهیه گزارش')),
                ('responsible1_signature', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='امضاء مسئول تهیه گزارش')),
                ('responsible2_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مسئول تایید گزارش')),
                ('responsible2_signature', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='امضاء مسئول تایید گزارش')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
