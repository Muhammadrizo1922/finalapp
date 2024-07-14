from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Tournament(models.Model):
   
   WEAPON = {
       'M416':'M416',
       'M24':'M24',
       'All': 'All'
   }

   SQUAD = {
       'Solo':'Solo',
       'Duo':'Duo',
       'Squad':'Squad'
   }

   id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
   tournament_name = models.CharField(max_length=50)
   Prize = models.CharField(max_length=50)
   tournament_image = models.ImageField(upload_to='tournament/',blank=True,null=True)
   tournament_note = models.TextField(blank=True,null=True)
   tournament_rules = models.TextField()
   participants = models.TextField()
   squad = models.CharField(max_length=30, choices=SQUAD)
   weapon = models.CharField(max_length=50, choices=WEAPON)
   started = models.BooleanField(blank=True,null=True)
   start_date = models.DateField(blank=True,null=True)
   end_date = models.DateField(blank=True,null=True)
   finished = models.BooleanField(blank=True,null=True)
   available = models.BooleanField()
   isfull = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)

   
   def save(self, *args, **kwargs):
       if self.finished == True:
           self.available = False
       else:
           self.available = True 
       super().save(*args, **kwargs)

   def __str__(self):
       return self.tournament_name

class MyApply(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    FullName = models.CharField(max_length=80)
    PubgName = models.CharField(max_length=50)
    PubgID = models.CharField(max_length=20)
    tournament_name = models.ForeignKey(Tournament,limit_choices_to={'finished': False}, on_delete=models.CASCADE)
    tgusername = models.CharField(max_length=50, null=True,blank=True)
    applydate = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.FullName

class Player(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    FullName = models.CharField(max_length=100)
    PubgName = models.CharField(max_length=100)
    PubgID = models.CharField(max_length=20)
    point = models.IntegerField(default=0, null=True,blank=True)
    played = models.IntegerField(default=0,null=True,blank=True)
    win = models.IntegerField(default=0,null=True,blank=True)
    lose = models.IntegerField(default=0,null=True,blank=True)
    trophy = models.IntegerField(default=0,null=True,blank=True)
    joined = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.FullName