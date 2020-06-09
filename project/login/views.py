from django.shortcuts import render

# Create your views here.

def login(request):
  return render(request, 'login.html', locals())

def privacy_policy(request):
  return render(request, 'privacy_policy.html', locals())