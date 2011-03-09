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
	players_list = Player.objects.all()
	
	return render_to_response('index.html', {'players_list': players_list})	

def charcreate(request):
	class_list = uClass.objects.all()

	return render_to_response('charcreate.html', {'class_list': class_list})

def auth(request):
	return HttpResponse("Click the link to authorize your foursquare account.  If you don't have one yet, this will help you create one. <a href='{% url foursquare_oauth_auth %}'>Login with foursquare</a>")

# for reference only
def detail(request, player_id):
    try:
        p = Player.objects.get(pk=Player_id)
    except Player.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'player': p})


