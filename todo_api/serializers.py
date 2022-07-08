from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Roles
from .models import Persions
from .models import Report1
from .models import Report2
from .models import Stations
from .models import Users
from .models import Location
from .models import form1 
from .models import form2
from .models import NonConfirmation

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ["ID", "roleType", "userID", "expireDate", "createTime"]
class PersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persions
        fields = ["ID", "firstName", "lastName", "accuption", "personelNumber", "phoneNumber", "eMailAddress", "managerID"]
class Report1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Report1
        fields = ["ID", "parentID", "stationID" , "locationID", "userID", "creationDate", "field_1", "field_n"]  
class Report2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Report2
        fields = ["ID", "parentID", "stationID" , "locationID", "userID", "creationDate", "field_1", "field_n"]
class StationsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Stations
        fields = ["ID", "name", "stationID", "personlnCharge", "Location", "gpsLocation"]
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["ID", "name", "familyName", "roleID", "phoneNumber", "eMailAddress", "expireDate", "isActive"]
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["ID", "rName", "parentID","description", "EmergencyContact"]
class form1Serializer(serializers.ModelSerializer):
    class Meta:
        model = form1
        fields = ["Month", "Region", "StationName", "Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7", "Row8", "Row9", "Row10", "ReportDate", "Responsible1Name", "Responsible1Signature", "Responsible2Name", "Responsible2Signature"]
class form2Serializer(serializers.ModelSerializer):
    class Meta:
        model = form2
        fields = ["Month", "Region", "StationName", "distance1", "distance2", "distance3", "ScrollingTime1", "ScrollingTime2", "ScrollingTime3", "Row7", " WaterHeight1", " WaterHeight2", " WaterHeight3", "ChannelDepth", "ChannelWidth", "ReportDate", "Responsible1Name", "Responsible1Signature","Responsible2Name", "Responsible2Signature",]
class NonConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonConfirmation
        fields = ["Reason"]