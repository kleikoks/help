from django.apps import AppConfig


class SmsConfig(AppConfig):
  name = 'project.sms'


default_app_config = 'project.sms.SmsConfig'
