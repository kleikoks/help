from django.apps import AppConfig


class LoginConfig(AppConfig):
  name = 'project.login'


default_app_config = 'project.login.LoginConfig'
