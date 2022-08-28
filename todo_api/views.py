from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import re_path as url # from django.conf.urls import url
from django.urls import path , include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required , user_passes_test , permission_required 
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.authtoken.views import ObtainAuthToken
from django.template import loader
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
from .models import Form3 , Form4
# from .serializers import RolesSerializer
# from .serializers import PersionsSerializer
# from .serializers import Report1Serializer
# from .serializers import Report2Serializer
# from .serializers import StationsSerializer
# from .serializers import UsersSerializer
# from .serializers import LocationSerializer
from .serializers import Form1Serializer
from .serializers import Form2Serializer
from .serializers import NonconfirmationSerializer
from .serializers import Form3Serializer
from .serializers import Form4Serializer
from .serializers import UserSerializer , GroupSerializer


# POST form1
@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, ])
# @permission_classes((IsAuthenticated))
def post_form1(request):
    data = {
            'month': request.data.get('month'), 
            'region': request.data.get('region'),
            'station_name': request.data.get('station_name'),
            'row1': request.data.get('row1'),
            'row2': request.data.get('row2'),
            'row3': request.data.get('row3'),
            'row4': request.data.get('row4'),
            'row5': request.data.get('row5'),
            'row6': request.data.get('row6'),
            'row7': request.data.get('row7'),
            'row8': request.data.get('row8'),
            'row9': request.data.get('row9'),
            'row10': request.data.get('row10'),
            'report_date': request.data.get('report_date'),
            'responsible1_name': request.data.get('responsible1_name'),
            'responsible1_signature': request.data.get('responsible1_signature'),
            'responsible2_name': request.data.get('responsible2_name'),
            'responsible2_signature': request.data.get('responsible2_signature'),
            'user': request.user.id
        }
    serializer = Form1Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # Response(serializer.data, status=status.HTTP_201_CREATED)
        return render(request , 'todo_api/forms1.html')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# POST form2
@api_view(['POST' , 'GET'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def post_form2(request):
    data = {
           'month': request.data.get('month'),
           'region': request.data.get('region'),
           'station_name': request.data.get('station_name'),
           'distance1': request.data.get('distance1'),
           'distance2': request.data.get('distance2'),
           'distance3': request.data.get('distance3'),
           'scrolling_time1': request.data.get('scrolling_time1'),
           'scrolling_time2': request.data.get('scrolling_time2'),
           'scrolling_time3': request.data.get('scrolling_time3'),
           'water_height1': request.data.get('water_height1'),
           'water_height2': request.data.get('water_height2'),
           'water_height3': request.data.get('water_height3'),
           'channel_depth': request.data.get('channel_depth'),
           'channel_width': request.data.get('channel_width'),
           'report_date': request.data.get('report_date'),
           'responsible1_name': request.data.get('responsible1_name'),
           'responsible1_signature': request.data.get('responsible1_signature'),
           'responsible2_name': request.data.get('responsible2_name'),
           'responsible2_signature': request.data.get('responsible2_signature'),
           'user': request.user.id
        }
    serializer = Form2Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return render(request , 'todo_api/forms1.html')
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    






#  POST NonConfirmation
@api_view(['POST'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def post_nonconfirmation(request):
    data = {
           'form' : request.data.get('form'),
           'date' : request.data.get('date'),
           'reason': request.data.get('reason'),
           'user': request.user.id
        }
    serializer = NonconfirmationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return render(request , 'todo_api/forms1.html')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    


# delete1
@api_view(['POST', 'GET','DELETE'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def delete(request, id):
      myform1 = Form1.objects.get(id=id)
      myform1.delete()
      return render(request , 'todo_api/forms1.html')
  
  
# delete2
@api_view(['POST', 'GET','DELETE'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def delete2(request, id):
      myform2 = Form2.objects.get(id=id)
      myform2.delete()
      return render(request , 'todo_api/forms1.html')
  
  
  # delete3
@api_view(['POST', 'GET','DELETE'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def delete3(request, id):
      myform3 = Nonconfirmation.objects.get(id=id)
      myform3.delete()
      return render(request , 'todo_api/forms1.html')
  
  
  
# update1
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update1(request, id):
    if request.user.is_authenticated and request.user.username != 'dashboard' :
        myform1 = Form1.objects.get(id=id)
        template = loader.get_template('update1.html')
        context = {
        'myform1' : myform1,
    }
        return HttpResponse(template.render(context, request))
    else:
        return render(request , 'todo_api/index.html')



#updaterecord1 , submit
@api_view(['POST', 'GET', 'PUT' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def updaterecord1(request, id): 
    month = request.POST['month']
    region = request.POST['region']
    station_name = request.POST['station_name']
    row1 = request.POST['row1']
    row2 = request.POST['row2']
    row3 = request.POST['row3']
    row4 = request.POST['row4']
    row5 = request.POST['row5']
    row6 = request.POST['row6']
    row7 = request.POST['row7']
    row8 = request.POST['row8']
    row9 = request.POST['row9']
    row10 = request.POST['row10']
    # report_date = request.POST['report_date']
    responsible1_name = request.POST['responsible1_name']
    responsible1_signature = request.POST['responsible1_signature']
    responsible2_name = request.POST['responsible2_name']
    responsible2_signature = request.POST['responsible2_signature']
    form1 = Form1.objects.get(id=id)
    form1.month = month
    form1.region = region
    form1.station_name = station_name
    form1.row1 = row1
    form1.row2 = row2
    form1.row3 = row3
    form1.row4 = row4
    form1.row5 = row5
    form1.row6 = row6
    form1.row7 = row7
    form1.row8 = row8
    form1.row9 = row9
    form1.row10 = row10
    # form1.report_date = report_date
    form1.responsible1_name = responsible1_name
    form1.responsible1_signature = responsible1_signature
    form1.responsible2_name = responsible2_name
    form1.responsible2_signature = responsible2_signature
    form1.save()
    return render(request , 'todo_api/forms1.html')




# update2
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update2(request, id):
    if request.user.is_authenticated and request.user.username != 'dashboard':
        myform2 = Form2.objects.get(id=id)
        template = loader.get_template('update2.html')
        context = {
        'myform2' : myform2,
    }
        return HttpResponse(template.render(context, request))
    else:
        return render(request , 'todo_api/index.html')



#updaterecord2 , submit
@api_view(['POST', 'GET', 'PUT' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def updaterecord2(request, id): 
    month = request.POST['month']
    region = request.POST['region']
    station_name = request.POST['station_name']
    distance1 = request.POST['distance1']
    distance2 = request.POST['distance2']
    distance3 = request.POST['distance3']
    scrolling_time1 = request.POST['scrolling_time1']
    scrolling_time2 = request.POST['scrolling_time2']
    scrolling_time3 = request.POST['scrolling_time3']
    water_height1 = request.POST['water_height1']
    water_height2 = request.POST['water_height2']
    water_height3 = request.POST['water_height3']
    channel_depth = request.POST['channel_depth']
    channel_width = request.POST['channel_width']
    # report_date = request.POST['report_date']
    responsible1_name = request.POST['responsible1_name']
    responsible1_signature = request.POST['responsible1_signature']
    responsible2_name = request.POST['responsible2_name']
    responsible2_signature = request.POST['responsible2_signature']
    form2 = Form2.objects.get(id=id)
    form2.month = month
    form2.region = region
    form2.station_name = station_name
    form2.distance1 = distance1
    form2.distance2 = distance2
    form2.distance3 = distance3
    form2.scrolling_time1 = scrolling_time1
    form2.scrolling_time2 = scrolling_time2
    form2.scrolling_time3 = scrolling_time3
    form2.water_height1 = water_height1
    form2.water_height2 = water_height2
    form2.water_height3 = water_height3
    form2.channel_depth = channel_depth
    form2.channel_width = channel_width
    # form2.report_date = report_date
    form2.responsible1_name = responsible1_name
    form2.responsible1_signature = responsible1_signature
    form2.responsible2_name = responsible2_name
    form2.responsible2_signature = responsible2_signature
    form2.save()
    return render(request , 'todo_api/forms1.html')





# index.html function
def index(request):
    return render(request , 'todo_api/index.html')




# form1.html function
@api_view(['POST', 'GET'])    
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form1(request):
    if request.user.is_authenticated and request.user.username != 'dashboard' and request.user.username != 'StaffSecretary' :
        return render(request , 'todo_api/form1.html')
    else:
        return render(request , 'todo_api/index.html')
    
    

# form2.html function 
@api_view(['POST', 'GET']) 
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form2(request):
    if request.user.is_authenticated and request.user.username != 'dashboard' and request.user.username != 'StaffSecretary' :
        return render(request , 'todo_api/form2.html')
    else:
        return render(request , 'todo_api/index.html')    
    
    
    
# form3.html function , get form1
@api_view(['POST', 'GET','DELETE']) 
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form3(request):
    if request.user.is_authenticated and request.user.username != 'dashboard' :
        myform1 = Form1.objects.all().values()
        template = loader.get_template('form3.html')
        context = {
        'myform1': myform1,
  }
        return HttpResponse(template.render(context, request))
    else:
        return render(request , 'todo_api/index.html')



# form4.html function , get form2
@api_view(['POST', 'GET','DELETE']) 
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form4(request):
    if request.user.is_authenticated and request.user.username != 'dashboard' :
        myform2 = Form2.objects.all().values()
        template = loader.get_template('form4.html')
        context = {
        'myform2': myform2,
  }
        return HttpResponse(template.render(context, request))
    else:
        return render(request , 'todo_api/index.html')



#form5.html 
@api_view(['POST', 'GET'])    
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form5(request):
    if request.user.is_authenticated and request.user.username != 'dashboard' and request.user.username != 'StationReportTransmitter':
        return render(request , 'todo_api/form5.html')
    else:
        return render(request , 'todo_api/index.html')
    
    
    
# form6.html function , get 
@api_view(['POST', 'GET','DELETE']) 
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form6(request):
    if request.user.is_authenticated and request.user.username != 'dashboard' :
        myform3 = Nonconfirmation.objects.all().values()
        template = loader.get_template('form6.html')
        context = {
        'myform3': myform3,
  }
        return HttpResponse(template.render(context, request))
    else:
        return render(request , 'todo_api/index.html')




#  function for logout
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def logout_user(request): 
    logout(request)
    return render(request , 'todo_api/index.html')


# update3
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update3(request, id):
    if request.user.is_authenticated and request.user.username != 'dashboard' and request.user.username != 'StationReportTransmitter' :
        myform3 = Form1.objects.get(id=id)
        template = loader.get_template('update3.html')
        context = {
        'myform3' : myform3,
    }
        return HttpResponse(template.render(context, request))
    else:
        return render(request , 'todo_api/index.html')




# تایید نهایی فرم یک
@api_view(['POST', 'GET', 'DELETE'])
@authentication_classes([SessionAuthentication, ])
# @permission_classes((IsAuthenticated))
def post_form3(request):
    data = {
            'month': request.data.get('month'), 
            'region': request.data.get('region'),
            'station_name': request.data.get('station_name'),
            'row1': request.data.get('row1'),
            'row2': request.data.get('row2'),
            'row3': request.data.get('row3'),
            'row4': request.data.get('row4'),
            'row5': request.data.get('row5'),
            'row6': request.data.get('row6'),
            'row7': request.data.get('row7'),
            'row8': request.data.get('row8'),
            'row9': request.data.get('row9'),
            'row10': request.data.get('row10'),
            'report_date': request.data.get('report_date'),
            'responsible1_name': request.data.get('responsible1_name'),
            'responsible1_signature': request.data.get('responsible1_signature'),
            'responsible2_name': request.data.get('responsible2_name'),
            'responsible2_signature': request.data.get('responsible2_signature'),
            'user': request.user.id
        }
    serializer = Form3Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # Response(serializer.data, status=status.HTTP_201_CREATED)
        return render(request , 'todo_api/forms1.html')
    
    
    
# update4
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update4(request, id):
    if request.user.is_authenticated and request.user.username != 'dashboard' and request.user.username != 'StationReportTransmitter' :
       myform4 = Form2.objects.get(id=id)
       template = loader.get_template('update4.html')
       context = {
        'myform4' : myform4,
    }
       return HttpResponse(template.render(context, request))
    else:
       return render(request , 'todo_api/index.html')


# تایید نهایی فرم دو
@api_view(['POST' , 'GET'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def post_form4(request):
    data = {
           'month': request.data.get('month'),
           'region': request.data.get('region'),
           'station_name': request.data.get('station_name'),
           'distance1': request.data.get('distance1'),
           'distance2': request.data.get('distance2'),
           'distance3': request.data.get('distance3'),
           'scrolling_time1': request.data.get('scrolling_time1'),
           'scrolling_time2': request.data.get('scrolling_time2'),
           'scrolling_time3': request.data.get('scrolling_time3'),
           'water_height1': request.data.get('water_height1'),
           'water_height2': request.data.get('water_height2'),
           'water_height3': request.data.get('water_height3'),
           'channel_depth': request.data.get('channel_depth'),
           'channel_width': request.data.get('channel_width'),
           'report_date': request.data.get('report_date'),
           'responsible1_name': request.data.get('responsible1_name'),
           'responsible1_signature': request.data.get('responsible1_signature'),
           'responsible2_name': request.data.get('responsible2_name'),
           'responsible2_signature': request.data.get('responsible2_signature'),
           'user': request.user.id
        }
    serializer = Form4Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return render(request , 'todo_api/forms1.html')
    
    
# form7.html function , get form1 final
@api_view(['POST', 'GET','DELETE']) 
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form7(request):
    if request.user.is_authenticated and request.user.username != 'StationReportTransmitter' and request.user.username != 'StaffSecretary' :
       myform7 = Form3.objects.all().values()
       template = loader.get_template('form7.html')
       context = {
       'myform7': myform7,
  }
       return HttpResponse(template.render(context, request))
    else:
       return render(request , 'todo_api/index.html')

# update5
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update5(request, id):
    if request.user.is_authenticated and request.user.username != 'StationReportTransmitter' and request.user.username != 'StaffSecretary' :
        myform5 = Form3.objects.get(id=id)
        template = loader.get_template('update5.html')
        context = {
        'myform5' : myform5,
    }
        return HttpResponse(template.render(context, request))
    else:
           return render(request , 'todo_api/index.html')



# form7.html function , get form1 final
@api_view(['POST', 'GET','DELETE']) 
@permission_classes((IsAuthenticated,))
@authentication_classes([SessionAuthentication, ])
def form8(request):
    if request.user.is_authenticated and request.user.username != 'StationReportTransmitter' and request.user.username != 'StaffSecretary' :
        myform8 = Form4.objects.all().values()
        template = loader.get_template('form8.html')
        context = {
        'myform8': myform8,
  }
        return HttpResponse(template.render(context, request))
    else:
           return render(request , 'todo_api/index.html')


# update6
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update6(request, id):
    if request.user.is_authenticated and request.user.username != 'StationReportTransmitter' and request.user.username != 'StaffSecretary' :
        myform6 = Form4.objects.get(id=id)
        template = loader.get_template('update6.html')
        context = {
        'myform6' : myform6,
    }
        return HttpResponse(template.render(context, request))
    else:
           return render(request , 'todo_api/index.html')


# delete final1 form3
@api_view(['POST', 'GET','DELETE'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def delete4(request, id):
      myform3 = Form3.objects.get(id=id)
      myform3.delete()
      return render(request , 'todo_api/forms1.html')
  
# update3 final1 form3
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update7(request, id):
    if request.user.is_authenticated and request.user.username != 'StationReportTransmitter' and request.user.username != 'StaffSecretary' and request.user.username != 'dashboard':
       myform3 = Form3.objects.get(id=id)
       template = loader.get_template('update7.html')
       context = {
        'myform3' : myform3,
    }
       return HttpResponse(template.render(context, request))
    else:
           return render(request , 'todo_api/index.html')


#updaterecord3 , final1 submit
@api_view(['POST', 'GET', 'PUT' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def updaterecord3(request, id): 
    month = request.POST['month']
    region = request.POST['region']
    station_name = request.POST['station_name']
    row1 = request.POST['row1']
    row2 = request.POST['row2']
    row3 = request.POST['row3']
    row4 = request.POST['row4']
    row5 = request.POST['row5']
    row6 = request.POST['row6']
    row7 = request.POST['row7']
    row8 = request.POST['row8']
    row9 = request.POST['row9']
    row10 = request.POST['row10']
    # report_date = request.POST['report_date']
    responsible1_name = request.POST['responsible1_name']
    responsible1_signature = request.POST['responsible1_signature']
    responsible2_name = request.POST['responsible2_name']
    responsible2_signature = request.POST['responsible2_signature']
    form3 = Form3.objects.get(id=id)
    form3.month = month
    form3.region = region
    form3.station_name = station_name
    form3.row1 = row1
    form3.row2 = row2
    form3.row3 = row3
    form3.row4 = row4
    form3.row5 = row5
    form3.row6 = row6
    form3.row7 = row7
    form3.row8 = row8
    form3.row9 = row9
    form3.row10 = row10
    # form1.report_date = report_date
    form3.responsible1_name = responsible1_name
    form3.responsible1_signature = responsible1_signature
    form3.responsible2_name = responsible2_name
    form3.responsible2_signature = responsible2_signature
    form3.save()
    return render(request , 'todo_api/forms1.html')



# delete final2 form4
@api_view(['POST', 'GET','DELETE'])
# @permission_classes((IsAuthenticated))
@authentication_classes([SessionAuthentication, ])
def delete5(request, id):
      myform4 = Form4.objects.get(id=id)
      myform4.delete()
      return render(request , 'todo_api/forms1.html')
  
  
  
  
# update3 final1 form3
@api_view(['PUT', 'GET' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def update8(request, id):
     if request.user.is_authenticated and request.user.username != 'StationReportTransmitter' and request.user.username != 'StaffSecretary' and request.user.username != 'dashboard':
         myform4 = Form4.objects.get(id=id)
         template = loader.get_template('update8.html')
         context = {
         'myform4' : myform4,
    }
         return HttpResponse(template.render(context, request))
     else:
           return render(request , 'todo_api/index.html')



#updaterecord4 , final2 submit
@api_view(['POST', 'GET', 'PUT' , 'DELETE'])
@authentication_classes([SessionAuthentication, ])
def updaterecord4(request, id): 
    month = request.POST['month']
    region = request.POST['region']
    station_name = request.POST['station_name']
    distance1 = request.POST['distance1']
    distance2 = request.POST['distance2']
    distance3 = request.POST['distance3']
    scrolling_time1 = request.POST['scrolling_time1']
    scrolling_time2 = request.POST['scrolling_time2']
    scrolling_time3 = request.POST['scrolling_time3']
    water_height1 = request.POST['water_height1']
    water_height2 = request.POST['water_height2']
    water_height3 = request.POST['water_height3']
    channel_depth = request.POST['channel_depth']
    channel_width = request.POST['channel_width']
    # report_date = request.POST['report_date']
    responsible1_name = request.POST['responsible1_name']
    responsible1_signature = request.POST['responsible1_signature']
    responsible2_name = request.POST['responsible2_name']
    responsible2_signature = request.POST['responsible2_signature']
    form4 = Form4.objects.get(id=id)
    form4.month = month
    form4.region = region
    form4.station_name = station_name
    form4.distance1 = distance1
    form4.distance2 = distance2
    form4.distance3 = distance3
    form4.scrolling_time1 = scrolling_time1
    form4.scrolling_time2 = scrolling_time2
    form4.scrolling_time3 = scrolling_time3
    form4.water_height1 = water_height1
    form4.water_height2 = water_height2
    form4.water_height3 = water_height3
    form4.channel_depth = channel_depth
    form4.channel_width = channel_width
    # form2.report_date = report_date
    form4.responsible1_name = responsible1_name
    form4.responsible1_signature = responsible1_signature
    form4.responsible2_name = responsible2_name
    form4.responsible2_signature = responsible2_signature
    form4.save()
    return render(request , 'todo_api/forms1.html')
        