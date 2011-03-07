# Crea
from fschatapp.models import Player
from fschatapp.models import uClass
from fschatapp.models import Attribute

from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world.")

def guest(request):
	return HttpResponse("Welcome to ZombiePirateNinjaRobot.com</br> (about the game) (registration form)<a href='/auth'>Go</a>")

def auth(request):
	return HttpResponse("Click the link to authorize your foursquare account.  If you don't have one yet, this will help you create one. <a href='https://foursquare.com/oauth2/access_token'>Connect to Foursquare</a>")

# for reference only
def detail(request, player_id):
    try:
        p = Player.objects.get(pk=Player_id)
    except Player.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'player': p})


