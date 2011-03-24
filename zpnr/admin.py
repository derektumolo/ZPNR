from zpnr.models import *
#import zpnr.models
#from zpnr.models import uClass
#from zpnr.models import Attribute
#from zpnr.models import playerAttr

from django.contrib import admin

#for fsmodel in dir(zpnr.models):
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

#admin.site.register(baseItemAttributes) #to record the attributes for a base 
	#item

admin.site.register(venueCategory)


