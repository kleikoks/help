from django.shortcuts import render
from django.conf import settings
from twilio.rest import Client
# Create your views here.


def send_sms(request):
  # client = Client('AC9861ce6fc83e2a700371bde633e0c619', '5f33e1786baddc5e913155c47edebb94')
  # message = client.messages.create(
  #                                   to='+380988811221',
  #                                   from_ = '+18327569282',
  #                                   body = 'my_msg'
  #                                 )
  return render(request, 'index.html', locals())
