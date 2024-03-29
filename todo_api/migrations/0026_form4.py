# Generated by Django 4.0.5 on 2022-08-27 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_api', '0025_alter_form1_report_date_alter_form2_report_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('station_name', models.CharField(blank=True, max_length=200, null=True)),
                ('distance1', models.FloatField(default=0, verbose_name='(فاصله بین دو نقطه(متر')),
                ('distance2', models.FloatField(default=0, verbose_name='(فاصله بین دو نقطه(متر')),
                ('distance3', models.FloatField(default=0, verbose_name='(فاصله بین دو نقطه(متر')),
                ('scrolling_time1', models.IntegerField(default=0, verbose_name='(زمان پیمایش(ثانیه')),
                ('scrolling_time2', models.IntegerField(default=0, verbose_name='(زمان پیمایش(ثانیه')),
                ('scrolling_time3', models.IntegerField(default=0, verbose_name='(زمان پیمایش(ثانیه')),
                ('water_height1', models.FloatField(default=0, verbose_name='(ارتفاع آب(متر')),
                ('water_height2', models.FloatField(default=0, verbose_name='(ارتفاع آب(متر')),
                ('water_height3', models.FloatField(default=0, verbose_name='(ارتفاع آب(متر')),
                ('channel_depth', models.FloatField(default=0, verbose_name='(عمق کانال(متر')),
                ('channel_width', models.FloatField(default=0, verbose_name='(عرض کانال(متر')),
                ('report_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ تهیه گزارش')),
                ('responsible1_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مسئول تهیه گزارش')),
                ('responsible1_signature', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='امضاء مسئول تهیه گزارش')),
                ('responsible2_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مسئول تایید گزارش')),
                ('responsible2_signature', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='امضاء مسئول تایید گزارش')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
