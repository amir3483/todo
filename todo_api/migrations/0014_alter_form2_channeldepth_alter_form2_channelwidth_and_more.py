# Generated by Django 4.0.5 on 2022-08-11 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0013_alter_form1_month_alter_form1_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='ChannelDepth',
            field=models.FloatField(blank=True, null=True, verbose_name='(عمق کانال(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='ChannelWidth',
            field=models.FloatField(blank=True, null=True, verbose_name='(عرض کانال(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='Month',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='form2',
            name='Region',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='form2',
            name='ReportDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ تهیه گزارش'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='Responsible1Name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مسئول تهیه گزارش'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='Responsible1Signature',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='امضاء مسئول تهیه گزارش'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='Responsible2Name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مسئول تایید گزارش'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='Responsible2Signature',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='امضاء مسئول تایید گزارش'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='ScrollingTime1',
            field=models.IntegerField(blank=True, null=True, verbose_name='(زمان پیمایش(ثانیه'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='ScrollingTime2',
            field=models.IntegerField(blank=True, null=True, verbose_name='(زمان پیمایش(ثانیه'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='ScrollingTime3',
            field=models.IntegerField(blank=True, null=True, verbose_name='(زمان پیمایش(ثانیه'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='StationName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='form2',
            name='WaterHeight1',
            field=models.FloatField(blank=True, null=True, verbose_name='(ارتفاع آب(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='WaterHeight2',
            field=models.FloatField(blank=True, null=True, verbose_name='(ارتفاع آب(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='WaterHeight3',
            field=models.FloatField(blank=True, null=True, verbose_name='(ارتفاع آب(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='distance1',
            field=models.FloatField(blank=True, null=True, verbose_name='(فاصله بین دو نقطه(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='distance2',
            field=models.FloatField(blank=True, null=True, verbose_name='(فاصله بین دو نقطه(متر'),
        ),
        migrations.AlterField(
            model_name='form2',
            name='distance3',
            field=models.FloatField(blank=True, null=True, verbose_name='(فاصله بین دو نقطه(متر'),
        ),
        migrations.AlterField(
            model_name='nonconfirmation',
            name='Reason',
            field=models.TextField(blank=True, null=True, verbose_name='علت عدم تایید'),
        ),
    ]
