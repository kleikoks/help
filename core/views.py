from django.shortcuts import render
from .tasks import *
# Create your views here.


def task(request):
  add_always.delay()
  return render(request, 'index.html', locals())
