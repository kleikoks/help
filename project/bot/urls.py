from django.contrib import admin
from django.urls import path, include
from .views import *

# viber
urlpatterns = [
    path('viber_bot/', viber_bot, name='viber_bot'),
]