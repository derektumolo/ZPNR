from fschatapp.models import *
#import fschatapp.models
#from fschatapp.models import uClass
#from fschatapp.models import Attribute
#from fschatapp.models import playerAttr

from django.contrib import admin

#for fsmodel in dir(fschatapp.models):
#	admin.site.register(fsmodel)

admin.site.register(Player)

admin.site.register(uClass)

admin.site.register(Attribute)

admin.site.register(playerAttr)

admin.site.register(Skill)

admin.site.register(playerSkill)

admin.site.register(baseItem)

admin.site.register(playerInv)

admin.site.register(itemType)

admin.site.register(playerQuest)

admin.site.register(Quest)

admin.site.register(Battle)

admin.site.register(itemTypeAttributes)

#admin.site.register(baseItemAttributes) #to record the attributes for a base itme

admin.site.register(venueCategory)


