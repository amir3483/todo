from django.db import models
from django.contrib.auth.models import User , Group
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
class form1(models.Model): #گزارش بازدید ماهانه از وضعیت سلامت ایستگاه
    Month = models.CharField(max_length = 50, blank = True)
    Region = models.CharField(max_length = 200, blank = True)
    StationName = models.CharField(max_length = 200, blank = True)
    Row1 = models.TextField(blank= True, verbose_name="قفل بودن درب محوطه ایستگاه")
    Row2 = models.TextField(blank = True, verbose_name="قفل بودن درب جعبه تجهیزات")
    Row3 = models.TextField(blank = True , verbose_name="عدم وجود آب، برف، علوفه، زباله، نخاله و... در محوطه ایستگاه و اطراف")
    Row4 = models.TextField(blank = True, verbose_name="عدم گسترش پوشش گیاهی موجود (درختان و ..). در محوطه و اطراف ایستگاه")
    Row5 = models.TextField(blank = True, verbose_name="عدم انجام عملیات عمرانی در محوطه ایستگاه و اطراف")
    Row6 = models.TextField(blank = True, verbose_name="عدم وجود هرگونه مانع و تجهیزات در مجاورت ایستگاه تا فاصله  2متری")
    Row7 = models.TextField(blank = True, verbose_name="کنترل وضعیت برق ایستگاه")
    Row8 = models.TextField(blank = True, verbose_name="وضعیت سیستمهای ارتباطی و آنتن خارجی")
    Row9 = models.TextField(blank = True, verbose_name="تعداد و تاریخ مراجعه اضطراری به ایستگاه")
    Row10 = models.TextField(blank = True, verbose_name="سایر موارد - موارد اعلامی از سوی سازمان")
    ReportDate = models.DateTimeField(null = True, verbose_name="تاریخ تهیه گزارش")
    Responsible1Name = models.CharField(max_length = 200, blank = True, verbose_name="نام مسئول تهیه گزارش")
    Responsible1Signature = models.ImageField(upload_to='images/' , verbose_name = "امضاء مسئول تهیه گزارش")
    Responsible2Name = models.CharField(max_length = 200, blank = True, verbose_name="نام مسئول تایید گزارش")
    Responsible2Signature = models.ImageField(upload_to='images/' , verbose_name = "امضاء مسئول تایید گزارش")
    
    def __str__(self):
        return self.StationName
    
class form2(models.Model ): # گزارش ثبت داده جهت مراجعه سرعت و دبی ایستگاه های سطح سنج
    Month = models.CharField(max_length = 50, blank = True)
    Region = models.CharField(max_length = 200, blank = True)
    StationName = models.CharField(max_length = 200, blank = True)
    distance1 = models.FloatField(null = True , verbose_name = '(فاصله بین دو نقطه(متر')
    distance2 = models.FloatField(null = True , verbose_name = '(فاصله بین دو نقطه(متر')
    distance3 = models.FloatField(null = True , verbose_name = '(فاصله بین دو نقطه(متر')
    ScrollingTime1 = models.IntegerField(null = True , verbose_name = '(زمان پیمایش(ثانیه')
    ScrollingTime2 = models.IntegerField(null = True , verbose_name = '(زمان پیمایش(ثانیه')
    ScrollingTime3 = models.IntegerField(null = True , verbose_name = '(زمان پیمایش(ثانیه')
    WaterHeight1 = models.FloatField(null = True , verbose_name = '(ارتفاع آب(متر')
    WaterHeight2 = models.FloatField(null = True , verbose_name = '(ارتفاع آب(متر')
    WaterHeight3 = models.FloatField(null = True , verbose_name = '(ارتفاع آب(متر')
    ChannelDepth = models.FloatField(null = True , verbose_name = '(عمق کانال(متر')
    ChannelWidth = models.FloatField(null = True , verbose_name = '(عرض کانال(متر')
    ReportDate = models.DateTimeField(null = True, verbose_name="تاریخ تهیه گزارش")
    Responsible1Name = models.CharField(max_length = 200, blank = True, verbose_name="نام مسئول تهیه گزارش")
    Responsible1Signature = models.ImageField(upload_to='images/' , verbose_name = "امضاء مسئول تهیه گزارش")
    Responsible2Name = models.CharField(max_length = 200, blank = True, verbose_name="نام مسئول تایید گزارش")
    Responsible2Signature = models.ImageField(upload_to='images/' , verbose_name = "امضاء مسئول تایید گزارش")
    
    def __str__(self):
        return self.StationName
# علت عدم تایید کاربر دبیر ستاد
class NonConfirmation(models.Model):
    Reason = models.TextField(blank = True, verbose_name='علت عدم تایید')
    
    def __str__(self):
        return self.Reason
    

