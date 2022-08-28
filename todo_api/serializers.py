from rest_framework import serializers
from django.contrib.auth.models import User, Group
# from .models import Roles
# from .models import Persions
# from .models import Report1
# from .models import Report2
# from .models import Stations
# from .models import Users
# from .models import Location
from .models import Form1
from .models import Form2
from .models import Nonconfirmation
from .models import Form3
from .models import Form4

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'        

# class RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = ["ID", "roleType", "userID", "expireDate", "createTime"]
# class PersionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Persions
#         fields = ["ID", "firstName", "lastName", "accuption", "personelNumber", "phoneNumber", "eMailAddress", "managerID"]
# class Report1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Report1
#         fields = ["ID", "parentID", "stationID" , "locationID", "userID", "creationDate", "field_1", "field_n"]  
# class Report2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Report2
#         fields = ["ID", "parentID", "stationID" , "locationID", "userID", "creationDate", "field_1", "field_n"]
# class StationsSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Stations
#         fields = ["ID", "name", "stationID", "personlnCharge", "Location", "gpsLocation"]
# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ["ID", "name", "familyName", "roleID", "phoneNumber", "eMailAddress", "expireDate", "isActive"]
# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ["ID", "rName", "parentID","description", "EmergencyContact"]
class Form1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form1
        fields = ["id", "month", "region", "station_name", "row1", "row2", "row3", "row4", "row5", "row6", "row7", "row8", "row9", "row10", "report_date", "responsible1_name", "responsible2_name", "user"]
class Form2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form2
        fields = ["id", "month", "region", "station_name", "distance1", "distance2", "distance3", "scrolling_time1", "scrolling_time2", "scrolling_time3", "water_height1", "water_height2", "water_height3", "channel_depth", "channel_width", "report_date", "responsible1_name", "responsible2_name", "user"]
class NonconfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nonconfirmation
        fields = ["id", "form" , "date" , "reason", "user"]
        
class Form3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form3
        fields = ["id", "month", "region", "station_name", "row1", "row2", "row3", "row4", "row5", "row6", "row7", "row8", "row9", "row10", "report_date", "responsible1_name", "responsible2_name", "user"]
        
class Form4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form4
        fields = ["id", "month", "region", "station_name", "distance1", "distance2", "distance3", "scrolling_time1", "scrolling_time2", "scrolling_time3", "water_height1", "water_height2", "water_height3", "channel_depth", "channel_width", "report_date", "responsible1_name", "responsible2_name", "user"]