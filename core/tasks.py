from .celery import app
from celery.decorators import task, periodic_task
from datetime import timedelta

@task(ignore_result=False)
def send_spam_email(user_email):
  return 'fqwqqqqqqqqqqqqqqqqqqqqqqq'

@task(name="sum_two_numbers")
def add(x, y):
  return x + y

@task(name='periodic_task')
def ddd():
  print('spam')
  
@periodic_task(run_every=timedelta(seconds=10))
def fwq():
  logger = cronjob.get_logger(**kwargs)
  logger.warn("Gatcha bitch")