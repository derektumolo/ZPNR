# Crea
from zpnr.models import Player
from zpnr.models import uClass
from zpnr.models import Attribute

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return HttpResponse("Hello, world.")

def guest(request):
	players_list = Player.objects.all()
	
	return render_to_response('index.html', {'players_list': players_list})	

def charcreate(request):
	if request.method == "GET":
		class_list = uClass.objects.all()

		return render_to_response('charcreate.html', 
			{'class_list': class_list},
			context_instance=RequestContext(request))

	elif request.method == "POST":
		class_list = uClass.objects.all()
		try:
			cclass = class_list.get(pk=request.POST['class'])
		except (KeyError, cclass.DoesNotExist):
			return render_to_response('charcreate.html', {
				'class_list': class_list, 
				'error_message': "You must select a class."
			}, context_instance=RequestContext(request))
		else:
			if request.user.is_authenticated():
				player = Player.objects.get(user=request.user.id)
				player.uClass = class_list.get(pk=request.POST['class'])
				player.save()
	
			#go to the checkin page
				return HttpResponseRedirect(reverse('zpnr.views.checkin'))

def checkin(request):
	player = Player.objects.get(user=request.user.id)
	
	return render_to_response('checkin.html',{'player_class': player.uClass})

def auth(request):
	return HttpResponse("Click the link to authorize your foursquare account.  
		If you don't have one yet, this will help you create one. <a href=
		'{% url foursquare_oauth_auth %}'>Login with foursquare</a>")

# for reference only
def detail(request, player_id):
    try:
        p = Player.objects.get(pk=Player_id)
    except Player.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'player': p})


