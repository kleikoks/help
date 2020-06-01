from django.shortcuts import render
from django.conf import settings
from twilio.rest import TwilioRestClient
# Create your views here.

client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_sms(request):
  my_msg = 'lalka'
  message = client.messages.create(
                                    to='+380988811221',
                                    from_ = settings.TWILIO_PHONE_NUMBER,
                                    body = my_msg
                                  )
  return render(request, 'index.html', locals())