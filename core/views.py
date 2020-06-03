from django.shortcuts import render
from .tasks import *
# Create your views here.

def index(request):
  return render(request, 'index.html', locals())

def task(request):
  add_always.delay()
  return render(request, 'index.html', locals())
