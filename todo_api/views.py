from django.shortcuts import render
from django.urls import re_path as url # from django.conf.urls import url
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
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
from .serializers import RolesSerializer
from .serializers import PersionsSerializer
from .serializers import Report1Serializer
from .serializers import Report2Serializer
from .serializers import StationsSerializer
from .serializers import UsersSerializer
from .serializers import LocationSerializer
from .serializers import form1Serializer
from .serializers import form2Serializer
from .serializers import NonConfirmationSerializer

class RolesListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class RolesDetailApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class PersionsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class PersionsDetailApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class Report1ListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class Report1DetailApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class Report2ListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class Report2DetailApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class StationsListApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class StationsDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class UsersListApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class UsersDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class LocationListApiView(APIView):
        # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class LocationDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class form1ListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class form1DetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class form2ListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class form2DetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class NonConfirmationListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
class NonConfirmationDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
# Create your views here.
