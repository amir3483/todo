from turtle import pu
from django.urls import re_path as url # from django.conf.urls import url
from django.urls import path, include
from requests import put
from django.contrib import admin
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('index' , views.index , name='index'),
    path('form1' , views.form1 , name='form1'),
    path('form2' , views.form2 , name='form2'),
    path('form3' , views.form3 , name='form3'), #get form1
    path('form4' , views.form4 , name='form4'), #get form2
    path('form5' , views.form5 , name='form5'),
    path('form6' , views.form6 , name='form6'), #get reason
    path('form7' , views.form7 , name='form7'),
    path('form8' , views.form8 , name='form8'),
    path('logout_user' , views.logout_user , name='logout_user'),
    path('post_form1' , views.post_form1 , name='post_form1'),
    path('post_form2' , views.post_form2 , name='post_form2'),
    path('delete/<int:id>' , views.delete , name='delete'),
    path('delete2/<int:id>' , views.delete2 , name='delete2'),
    path('delete3/<int:id>' , views.delete3 , name='delete3'),
    path('delete4/<int:id>' , views.delete4 , name='delete4'),
    path('delete5/<int:id>' , views.delete5 , name='delete5'),
    path('update1/<int:id>', views.update1 , name='update1'),
    path('update1/updaterecord1/<int:id>', views.updaterecord1, name='updaterecord1'),
    path('update2/<int:id>', views.update2 , name='update2'),
    path('update2/updaterecord2/<int:id>', views.updaterecord2 , name='updaterecord2'),
    path('update7/updaterecord3/<int:id>', views.updaterecord3 , name='updaterecord3'),
    path('update8/updaterecord4/<int:id>', views.updaterecord4 , name='updaterecord4'),
    path('post_nonconfirmation' , views.post_nonconfirmation , name='post_nonconfirmation'),
    path('update3/<int:id>' , views.update3 , name='update3'),
    path('post_form3' , views.post_form3 , name='post_form3'),
    path('update4/<int:id>' , views.update4 , name='update4'),
    path('post_form4' , views.post_form4 , name='post_form4'),
    path('update5/<int:id>' , views.update5 , name='update5'),
    path('update6/<int:id>' , views.update6 , name='update6'),
    path('update7/<int:id>' , views.update7 , name='update7'),
    path('update8/<int:id>' , views.update8 , name='update8'),
]