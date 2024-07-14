from django.db import models
import uuid
from round.models import Round

class Match(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    player_1 = models.CharField(max_length=50)
    player_2 = models.CharField(max_length=50)
    forround = models.ForeignKey(Round,limit_choices_to={'finished': False}, on_delete=models.CASCADE)
    overall_1 = models.IntegerField(default=0,blank=True, null=True)
    overall_2 = models.IntegerField(default=0,blank=True, null=True)
    matchvideo = models.CharField(max_length=200, blank=True, null=True)
    tournament_winner = models.CharField(max_length=50,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

