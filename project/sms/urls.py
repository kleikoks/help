from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('send_sms/', send_sms, name='send_sms'),
]