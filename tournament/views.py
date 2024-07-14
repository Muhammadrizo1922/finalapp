from django.shortcuts import render,redirect
from .models import Tournament,Player, MyApply
from round.models import Round
from .forms import MyApplyForm

def index(request):
    tournaments = Tournament.objects.all().filter(finished=False)
    context = {'tours':tournaments}
    return render(request, 'index.html',context)

def tourdetail(request,tour_id):
    tour = Tournament.objects.get(id=tour_id)
    rounds = Round.objects.all().filter(tournament=tour).order_by('date')
    context = {'tournament':tour, 'rounds':rounds}
    return render(request, 'tournament/tourdetail.html', context)

def myapply(request):
    if request.method == 'POST':
        form = MyApplyForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            if Player.objects.filter(PubgID=new.PubgID).exists():
                new.save()
                return redirect('index')
            else:
                new.save()
                Player.objects.create(FullName=new.FullName,PubgName=new.PubgName,PubgID=new.PubgID)
                return redirect('index')
    else:
        form = MyApplyForm()
    context = {'form': form}
    return render(request, 'tournament/apply.html', context)


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        tours = Tournament.objects.filter(tournament_name__contains=search)
        players = Player.objects.filter(FullName__contains=search)
        return render(request, 'search.html', {'tours':tours,'players':players,'search':search})
    else:
        return render(request, 'search.html',)  

def playerinfo(request,plr_id):
    player = Player.objects.get(id=plr_id)
    context = {'player':player}
    return render(request, 'tournament/player.html', context)
