from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^fschat/', include('fschat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^User/$', 'zpnr.views.index'),
    (r'^User/(?P<user_id>\d+)/$', 'zpnr.views.detail'),

    # member page.  get to this later.  must include a notifications area.
    #    (r'^$', 'zpnr.views.member'),

    # home page first.  will need to add code that checks if you are logged 
    # in, and pushes you into the member page.
    # this page will include the registration form.
    (r'^$', 'zpnr.views.guest'), 
    (r'^/$', 'zpnr.views.guest'),

    # foursquare auth. first thing after reg.
    #    (r'^auth$', 'zpnr.views.auth'),

    #django foursquare
    (r'^auth/', include('djangofoursquare.urls')),

	# foursquare auth results and class selection.
	# here is also where we request location data, and explain what we use it
	# for.
    (r'^charcreate$', 'zpnr.views.charcreate'),

	# later, initial equip and other character creation

	# for now, jump straight to venue selection. may need sheisty code so its 
	# different the first time
    (r'^checkin/$', 'zpnr.views.checkin'),

	# venue confirm page.  details of the venue, and button to check in.
	#    (r'^venue/(?P<venue_id>\d+)/$', 'zpnr.views.venuesconfirm'),

	# checkin results and activity tabs for people, shop, quests, wilds.  need 
	# a notification area also.
	#    (r'^venue/(?P<venue_id>\d+)/results$', 'zpnr.views.venuesresults'),

	# ** social tools
	# battle
	#    (r'^battle/(?P<player_id>\d+)/$', 'zpnr.views.battle'),

	# battle results
	#    (r'^battle/(?P<player_id>\d+)/results$', 'zpnr.views.battleresults'),

	# invite
	#    (r'^invite/(?P<fs_id>\d+)/$', 'zpnr.views.invite'),

	# invite sent
	#    (r'^invite/(?P<fs_id>\d+)/results$', 'zpnr.views.inviteresults'),

	#trade
	#    (r'^trade/(?P<player_id>\d+)/$', 'zpnr.views.trade'),

	#trade sent,
	#    (r'^trade/(?P<player_id>\d+)/results$', 'zpnr.views.traderesults'),

	#**NPC stuff
	#shop
	#    (r'^shop/(?P<venue_id>\d+)/$', 'zpnr.views.shop'),

	#shop results
	#    (r'^shop/(?P<venue_id>\d+)/results$', 'zpnr.views.shopresults'),

	#quests
	#    (r'^quest/(?P<venue_id>\d+)/$', 'zpnr.views.quest'),

	#quest results
	#    (r'^quest/(?P<player_id>\d+)/results$', 'zpnr.views.questresults'),

	#wilds
	#    (r'^wilds/(?P<venue_id>\d+)/$', 'zpnr.views.wilds'),

	#wilds results
	#    (r'^wilds/(?P<venue_id>\d+)/results$', 'zpnr.views.wildsresults'),

)
