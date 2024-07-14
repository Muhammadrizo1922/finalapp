from django.shortcuts import render
from match.models import Match
from .models import Round

def roundmatches(request, rnd_id):
    forround = Round.objects.get(id=rnd_id)
    matches = Match.objects.all().filter(forround=forround)
    context = {'matches':matches}
    return render(request, 'tournament/matches.html',context)
