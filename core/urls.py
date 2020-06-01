from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('', include('project.bot.urls')),
]


# allauth
urlpatterns += [
    path('accounts/', include('allauth.urls')),
]
#SMS
urlpatterns += [
    path('messaging/', include('dj_twilio_sms.urls')),
]
TWILIO_ACCOUNT_SID = 'AC9861ce6fc83e2a700371bde633e0c619'
TWILIO_AUTH_TOKEN = '0e968e322a070554b8d31547b4303f2a'
TWILIO_PHONE_NUMBER '+18327569282'
TWILIO_CALLBACK_USE_HTTPS = False