from django.db import models

# Create your models here.

class Bot(models.Model):
  class Meta:
    verbose_name = 'Користувач'
    verbose_name_plural = 'Користувачі'
    
  user_id   = models.IntegerField(
    verbose_name = 'ID користувача'
    )