from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class parts_of_speach(models.Model):
    p_id=models.AutoField(primary_key=True)
    part_of_speach=models.CharField(max_length=20)

class dictionary(models.Model):
    id = models.AutoField(primary_key=True)
    word=models.CharField(max_length=20)
    characteristic=models.CharField(max_length=20)
    searched=models.IntegerField()
    p_id=models.ForeignKey(parts_of_speach, on_delete=models.CASCADE)

class initiators(models.Model):
    id=models.AutoField(primary_key=True)
    initiator=models.CharField(max_length=20)

class missing(models.Model):
    word=models.CharField(max_length=20,primary_key=True)
    initiated_by=models.ForeignKey(initiators, on_delete=models.CASCADE)
    times=models.IntegerField()

class generations(models.Model):
    word=models.CharField(max_length=20,primary_key=True)
    initiated_by=models.ForeignKey(initiators, on_delete=models.CASCADE)
    p_id=models.ForeignKey(parts_of_speach, on_delete=models.CASCADE)
    times=models.IntegerField()

