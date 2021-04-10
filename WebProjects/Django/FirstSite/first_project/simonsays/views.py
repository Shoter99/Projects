from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Player
from .forms import PlayerLogin
# Create your views here.

def index(response, name):
    try:
        p = Player.objects.get(nickname=name)
    except Exception as e:
        return HttpResponseRedirect("/simonsays/log")
    return render(response, 'index.html', {'player':p})
@csrf_exempt
def login(response):
    if response.method == 'POST':
        form = PlayerLogin(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            if Player.objects.get(nickname=n):
                p = Player.objects.get(nickname=n)
                return HttpResponseRedirect("/simonsays/game/"+p.nickname)

            player = Player(nickname=n)
            player.save()

            return HttpResponseRedirect("/simonsays/game/"+n)
    form = PlayerLogin()
    return render(response, 'login.html', {"login":form})
