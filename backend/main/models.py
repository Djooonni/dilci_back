from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class gps_data(models.Model):
    data_id = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class sayqac_data(models.Model):
    data_id = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
