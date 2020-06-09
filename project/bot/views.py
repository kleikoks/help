# viber
import requests
import json

from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': '4ba6245c5be7d3b3-ac0c6c57f0c614ee-bee1ac0907836e8e'}
bot_configuration = BotConfiguration(
  name='Dawn',
  avatar='http://viber.com/avatar.jpg',
  auth_token='4ba6245c5be7d3b3-ac0c6c57f0c614ee-bee1ac0907836e8e'
)
viber = Api(bot_configuration)

@csrf_exempt
def viber_bot_webhook(request):
  # sen = dict(
  #           url='https://kleikoks.fun/viber_bot_webhook/',
  #           event_types = ['unsubscribed', 'conversation_started', 'message', 'seen', 'delivered'],
  #           send_name = True,
  #           send_photo = True
  #           )
  # r = requests.post(hook, json.dumps(sen), headers=headers)
  # r = r.json()

  viber.set_webhook('https://kleikoks.fun/viber_bot/')
  return render(request, 'viber_bot.html', locals())


def viber_bot(request):
  if request.method == "POST":
    viber = json.loads(request.body.decode('utf-8'))
    if viber['event'] == 'webhook':
      return HttpResponse(status=200)
    else:
      return HttpResponse(status=500)
  return HttpResponse(status=200)

# telegram
import telebot
from django.conf import settings
from .models import Bot

bot   = telebot.TeleBot(settings.TOKEN)

def send_tele_spam(request):
  for user in Bot.objects.all():
    bot.send_message(user.user_id, 'text')

# main bot function
# @bot.message_handler(commands=['start'])
# def start_message(message):
#   bot.send_message(message.chat.id, 'По IP вичислю')
#   Bot.objects.get_or_create(
#     user_id = message.chat.id,
#   )
# bot.polling()