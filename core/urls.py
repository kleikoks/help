from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('', include('project.bot.urls')),
    path('', include('project.login.urls')),
]


#SMS
urlpatterns += [
    path('', include('project.sms.urls')),
    path('task/', task, name='task'),
]
#Facebook
urlpatterns += [
    path('facebook/', include('django_facebook.urls')),
]
#OATUH

urlpatterns += [
    path('social-auth/', include('social_django.urls', namespace="social")),
]