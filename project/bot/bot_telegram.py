import telebot
from django.conf import settings
from .models import Bot

bot   = telebot.TeleBot(settings.TOKEN)

def send_tele_spam(request):
  for user in Bot.objects.all():
    bot.send_message(user.user_id, 'text')

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, 'По IP вичислю')
  Bot.objects.get_or_create(
    user_id = message.chat.id,
  )
