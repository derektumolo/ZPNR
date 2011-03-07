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
    
    (r'^User/$', 'fschatapp.views.index'),
    (r'^User/(?P<user_id>\d+)/$', 'fschatapp.views.detail'),

# member page.  get to this later.  must include a notifications area.
#    (r'^$', 'fschatapp.views.member'),

# home page first.  will need to add code that checks if you are logged in, and pushes you into the member page.
# this page will include the registration form.
    (r'^$', 'fschatapp.views.guest'), 
    (r'^/$', 'fschatapp.views.guest'),

#foursquare auth. first thing after reg.
    (r'^auth$', 'fschatapp.views.auth'),

#foursquare auth results and class selection.
#here is also where we request location data, and explain what we use it for.
    (r'^charcreate$', 'fschatapp.views.charcreate'),

#later, initial equip and other character creation

#for now, jump straight to venue selection. may need sheisty code so its different the first time
    (r'^checkin$', 'fschatapp.views.checkin'),

#venue confirm page.  details of the venue, and button to check in.
    (r'^venue/(?P<venue_id>\d+)/$', 'fschatapp.views.venuesconfirm'),

#checkin results and activity tabs for people, shop, quests, wilds.  need a notification area also.
    (r'^venue/(?P<venue_id>\d+)/results$', 'fschatapp.views.venuesresults'),

#** social tools
#battle
    (r'^battle/(?P<player_id>\d+)/$', 'fschatapp.views.battle'),

#battle results
    (r'^battle/(?P<player_id>\d+)/results$', 'fschatapp.views.battleresults'),

#invite
    (r'^invite/(?P<fs_id>\d+)/$', 'fschatapp.views.invite'),

#invite sent
    (r'^invite/(?P<fs_id>\d+)/results$', 'fschatapp.views.inviteresults'),

#trade
    (r'^trade/(?P<player_id>\d+)/$', 'fschatapp.views.trade'),

#trade sent,
    (r'^trade/(?P<player_id>\d+)/results$', 'fschatapp.views.traderesults'),

#**NPC stuff
#shop
    (r'^shop/(?P<venue_id>\d+)/$', 'fschatapp.views.shop'),

#shop results
    (r'^shop/(?P<venue_id>\d+)/results$', 'fschatapp.views.shopresults'),

#quests
    (r'^quest/(?P<venue_id>\d+)/$', 'fschatapp.views.quest'),

#quest results
    (r'^quest/(?P<player_id>\d+)/results$', 'fschatapp.views.questresults'),

#wilds
    (r'^wilds/(?P<venue_id>\d+)/$', 'fschatapp.views.wilds'),

#wilds results
    (r'^wilds/(?P<venue_id>\d+)/results$', 'fschatapp.views.wildsresults'),

)
