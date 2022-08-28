from datetime import datetime
from django.db import models
from django.contrib.auth.models import User , Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Tables-1
class Roles(models.Model):
    ID = models.IntegerField(primary_key=True)
    roleType = models.CharField(max_length=200, blank= True)
    userID = models.IntegerField(null = True)
    expireDate = models.DateTimeField(null = True)
    createTime = models.DateTimeField(null = True)
    
    def __str__(self):
        return self.roleType
    
class Persions(models.Model):
    ID = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length = 200, blank = True)
    lastName = models.CharField(max_length = 200, blank = True)
    accuption = models.CharField(max_length = 200, blank = True)
    personelNumber = models.CharField(max_length = 200, blank = True)
    phoneNumber = models.CharField(max_length = 200, blank = True)
    eMailAddress = models.EmailField(blank = True)
    managerID = models.IntegerField(blank = True, null = True)
    
    def __str__(self):
        return self.lastName
    
class Report1(models.Model):
    ID = models.IntegerField(primary_key = True)
    parentID = models.IntegerField(null = True)
    stationID = models.IntegerField(null = True)
    locationID = models.IntegerField(null = True)
    userID = models.IntegerField(null = True)
    creationDate = models.DateTimeField(blank=True)
    field_1 = models.CharField(max_length = 200, blank = True)
    field_n = models.CharField(max_length = 200, blank = True)
        
    def __str__(self):
        return self.userID
    
class Report2(models.Model):
    ID = models.IntegerField(primary_key = True)
    parentID = models.IntegerField(null = True)
    stationID = models.IntegerField(null = True)
    locationID = models.IntegerField(null = True)
    userID = models.IntegerField(null = True)
    creationDate = models.DateTimeField(blank=True)
    field_1 = models.IntegerField(null = True)
    field_n = models.IntegerField(null = True)
        
    def __str__(self):
        return self.userID

class Stations(models.Model):
        ID = models.IntegerField(primary_key = True)
        name = models.CharField(max_length = 200, blank = True)
        stationID = models.CharField(max_length = 200, blank = True)
        personlnCharge = models.IntegerField(null = True)
        Location = models.CharField(max_length = 200, blank = True)
        gpsLocation = models.CharField(max_length = 200, blank = True)
        
        def __str__(self):
            return self.name
        
class Users(models.Model):
    ID = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200, blank = True)
    familyName = models.CharField(max_length = 200, blank = True)
    roleID = models.IntegerField(null = True)
    phoneNumber = models.CharField(max_length = 200, blank = True)
    eMailAddress = models.EmailField(blank = True)
    expireDate = models.DateTimeField(null = True)
    isActive : models.BooleanField(blank = True)
    
    def __str__(self):
        return self.familyName
    
class Location(models.Model):
    ID = models.IntegerField(primary_key = True)
    rName = models.CharField(max_length = 200, blank = True)
    parentID = models.IntegerField(null = True)
    description = models.IntegerField(null = True)
    EmergencyContact = models.IntegerField(null = True)
    
    def __str__(self):
        return self.rName
    
# Observatios-report-form
class Form1(models.Model): #گزارش بازدید ماهانه از وضعیت سلامت ایستگاه
    month = models.CharField(max_length = 50, blank = True, null = True)
    region = models.CharField(max_length = 200, blank = True, null = True)
    station_name = models.CharField(max_length = 200, blank = True, null = True)
    row1 = models.TextField(blank= True, null= True, verbose_name="قفل بودن درب محوطه ایستگاه")
    row2 = models.TextField(blank = True, null=True, verbose_name="قفل بودن درب جعبه تجهیزات")
    row3 = models.TextField(blank = True , null= True, verbose_name="عدم وجود آب، برف، علوفه، زباله، نخاله و... در محوطه ایستگاه و اطراف")
    row4 = models.TextField(blank = True, null= True, verbose_name="عدم گسترش پوشش گیاهی موجود (درختان و ..). در محوطه و اطراف ایستگاه")
    row5 = models.TextField(blank = True, null= True, verbose_name="عدم انجام عملیات عمرانی در محوطه ایستگاه و اطراف")
    row6 = models.TextField(blank = True, null= True, verbose_name="عدم وجود هرگونه مانع و تجهیزات در مجاورت ایستگاه تا فاصله  2متری")
    row7 = models.TextField(blank = True, null= True, verbose_name="کنترل وضعیت برق ایستگاه")
    row8 = models.TextField(blank = True, null= True, verbose_name="وضعیت سیستمهای ارتباطی و آنتن خارجی")
    row9 = models.TextField(blank = True, null= True, verbose_name="تعداد و تاریخ مراجعه اضطراری به ایستگاه")
    row10 = models.TextField(blank = True, null= True, verbose_name="سایر موارد - موارد اعلامی از سوی سازمان")
    report_date = models.DateTimeField(auto_now_add= True, null=True, verbose_name="تاریخ تهیه گزارش")
    responsible1_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تهیه گزارش")
    responsible1_signature = models.FileField(upload_to='files/' , verbose_name = "امضاء مسئول تهیه گزارش" , blank = True, null= True)
    responsible2_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تایید گزارش")
    responsible2_signature = models.FileField(upload_to='files/' , verbose_name = "امضاء مسئول تایید گزارش" , blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.station_name
    
class Form2(models.Model ): # گزارش ثبت داده جهت مراجعه سرعت و دبی ایستگاه های سطح سنج
    month = models.CharField(max_length = 50, blank = True, null = True)
    region = models.CharField(max_length = 200, blank = True, null= True)
    station_name = models.CharField(max_length = 200, blank = True, null= True)
    distance1 = models.FloatField(default=0, verbose_name = '(فاصله بین دو نقطه(متر')
    distance2 = models.FloatField(default=0, verbose_name = '(فاصله بین دو نقطه(متر')
    distance3 = models.FloatField(default=0, verbose_name = '(فاصله بین دو نقطه(متر')
    scrolling_time1 = models.IntegerField(default=0, verbose_name = '(زمان پیمایش(ثانیه')
    scrolling_time2 = models.IntegerField(default=0, verbose_name = '(زمان پیمایش(ثانیه')
    scrolling_time3 = models.IntegerField(default=0, verbose_name = '(زمان پیمایش(ثانیه')
    water_height1 = models.FloatField(default=0, verbose_name = '(ارتفاع آب(متر')
    water_height2 = models.FloatField(default=0, verbose_name = '(ارتفاع آب(متر')
    water_height3 = models.FloatField(default=0, verbose_name = '(ارتفاع آب(متر')
    channel_depth = models.FloatField(default=0, verbose_name = '(عمق کانال(متر')
    channel_width = models.FloatField(default=0, verbose_name = '(عرض کانال(متر')
    report_date = models.DateTimeField(auto_now_add= True,null=True, verbose_name="تاریخ تهیه گزارش")
    responsible1_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تهیه گزارش")
    responsible1_signature = models.FileField(upload_to='files/', verbose_name = "امضاء مسئول تهیه گزارش", blank = True, null = True,)
    responsible2_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تایید گزارش")
    responsible2_signature = models.FileField(upload_to='files/' , verbose_name = "امضاء مسئول تایید گزارش", blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.station_name
# علت عدم تایید کاربر دبیر ستاد
class Nonconfirmation(models.Model):
    form = models.CharField(max_length = 200, blank = True, null = True, verbose_name = "شماره فرم")
    date = models.DateTimeField(default=datetime.now, verbose_name="تاریخ")
    reason = models.TextField(blank = True, null= True, verbose_name='علت عدم تایید')
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.form
    
class Form3(models.Model): #گزارش بازدید ماهانه از وضعیت سلامت ایستگاه
    month = models.CharField(max_length = 50, blank = True, null = True)
    region = models.CharField(max_length = 200, blank = True, null = True)
    station_name = models.CharField(max_length = 200, blank = True, null = True)
    row1 = models.TextField(blank= True, null= True, verbose_name="قفل بودن درب محوطه ایستگاه")
    row2 = models.TextField(blank = True, null=True, verbose_name="قفل بودن درب جعبه تجهیزات")
    row3 = models.TextField(blank = True , null= True, verbose_name="عدم وجود آب، برف، علوفه، زباله، نخاله و... در محوطه ایستگاه و اطراف")
    row4 = models.TextField(blank = True, null= True, verbose_name="عدم گسترش پوشش گیاهی موجود (درختان و ..). در محوطه و اطراف ایستگاه")
    row5 = models.TextField(blank = True, null= True, verbose_name="عدم انجام عملیات عمرانی در محوطه ایستگاه و اطراف")
    row6 = models.TextField(blank = True, null= True, verbose_name="عدم وجود هرگونه مانع و تجهیزات در مجاورت ایستگاه تا فاصله  2متری")
    row7 = models.TextField(blank = True, null= True, verbose_name="کنترل وضعیت برق ایستگاه")
    row8 = models.TextField(blank = True, null= True, verbose_name="وضعیت سیستمهای ارتباطی و آنتن خارجی")
    row9 = models.TextField(blank = True, null= True, verbose_name="تعداد و تاریخ مراجعه اضطراری به ایستگاه")
    row10 = models.TextField(blank = True, null= True, verbose_name="سایر موارد - موارد اعلامی از سوی سازمان")
    report_date = models.DateTimeField(auto_now_add= True, null= True, verbose_name="تاریخ تهیه گزارش")
    responsible1_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تهیه گزارش")
    responsible1_signature = models.FileField(upload_to='files/' , verbose_name = "امضاء مسئول تهیه گزارش" , blank = True, null= True)
    responsible2_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تایید گزارش")
    responsible2_signature = models.FileField(upload_to='files/' , verbose_name = "امضاء مسئول تایید گزارش" , blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.station_name
    

    

class Form4(models.Model ): # گزارش ثبت داده جهت مراجعه سرعت و دبی ایستگاه های سطح سنج
    month = models.CharField(max_length = 50, blank = True, null = True)
    region = models.CharField(max_length = 200, blank = True, null= True)
    station_name = models.CharField(max_length = 200, blank = True, null= True)
    distance1 = models.FloatField(default=0, verbose_name = '(فاصله بین دو نقطه(متر')
    distance2 = models.FloatField(default=0, verbose_name = '(فاصله بین دو نقطه(متر')
    distance3 = models.FloatField(default=0, verbose_name = '(فاصله بین دو نقطه(متر')
    scrolling_time1 = models.IntegerField(default=0, verbose_name = '(زمان پیمایش(ثانیه')
    scrolling_time2 = models.IntegerField(default=0, verbose_name = '(زمان پیمایش(ثانیه')
    scrolling_time3 = models.IntegerField(default=0, verbose_name = '(زمان پیمایش(ثانیه')
    water_height1 = models.FloatField(default=0, verbose_name = '(ارتفاع آب(متر')
    water_height2 = models.FloatField(default=0, verbose_name = '(ارتفاع آب(متر')
    water_height3 = models.FloatField(default=0, verbose_name = '(ارتفاع آب(متر')
    channel_depth = models.FloatField(default=0, verbose_name = '(عمق کانال(متر')
    channel_width = models.FloatField(default=0, verbose_name = '(عرض کانال(متر')
    report_date = models.DateTimeField(auto_now_add= True,null=True, verbose_name="تاریخ تهیه گزارش")
    responsible1_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تهیه گزارش")
    responsible1_signature = models.FileField(upload_to='files/', verbose_name = "امضاء مسئول تهیه گزارش", blank = True, null = True,)
    responsible2_name = models.CharField(max_length = 200, blank = True, null= True, verbose_name="نام مسئول تایید گزارش")
    responsible2_signature = models.FileField(upload_to='files/' , verbose_name = "امضاء مسئول تایید گزارش", blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.station_name