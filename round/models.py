from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from tournament.models import Tournament

class Round(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    round_number = models.CharField(max_length=35)
    tournament = models.ForeignKey(Tournament,limit_choices_to={'finished': False}, on_delete=models.CASCADE)
    current = models.BooleanField(blank=True,null=True)
    finished = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return self.round_number