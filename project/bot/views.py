# viber
import requests
import json

from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

auth_token = '4b88a58f1de7d33b-2dc87d48a643f917-659644b299fe82e9'
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}

viber = BotConfiguration(
	name = 'tivtir',
	avatar = 'http://viber.com/avatar.jpg',
	auth_token = auth_token
)

def viber_bot(request):
  sen = dict(
            url='https://kleikoks.fun',
            event_types = ['unsubscribed', 'conversation_started', 'message', 'seen', 'delivered'],
            send_name = True,
            send_photo = True
            )
  r = requests.post(hook, json.dumps(sen), headers=headers)
  print(r.json())
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