from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Attribute (models.Model):
	#this class just sets names for attributes.  
	attr_name = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.attrName	

class PlayerAttr (models.Model):
	# many to many relationship, allows setting a player's attrs.
	user_attribute = models.ForeignKey(Attribute)
	player = models.ForeignKey('Player')
	value = models.IntegerField()
	
	#def __unicode__(self):
		#don't want to figure this out just yet, but this should be
		#returning Player:Attribute:Value 
	#	return self.value

class UserClass (models.Model):
	verbose_name = "Class"
	verbose_name = "Classes"	

	class_name = models.CharField(max_length = 200)
	class_primary_attr = models.ForeignKey(Attribute, 
		related_name='primary_classes')

	class_secondary_attr = models.ForeignKey(Attribute, 
		related_name='secondary classes')
	
	def __unicode__(self):
		#later: <classname>: primary - <primary, secondary - <second
		return self.class_name	

class Skill (models.Model):
	skill_name = models.CharField(max_length = 200)
	skill_desc = models.CharField(max_length = 200)
	
	hp_dmg = models.IntegerField()
	mp_dmg = models.IntegerField()
	hp_absorb = models.IntegerField()
	ap_dmg = models.IntegerField()
	
	hp_cost = models.IntegerField()
	mp_cost = models.IntegerField()
	ap_cost = models.IntegerField()

	# later, status effects. blocking isn't possible with this system

	def __unicode__(self):
		return self.skill_name	

class PlayerManager(models.Manager):
    def create_player(self, fsid, fstoken):
        """
        Creates and saves a Player with the given fs info
        """

        now = datetime.datetime.now()

        # Normalize the address by lowercasing the domain part of the email
        # address.

        player = self.model(foursquareId=fsid, foursquareToken=fstoken)

        player.save(using=self._db)
        return player

class Player (models.Model):
	player_name = models.CharField(max_length = 200)
	player_password = models.CharField(max_length = 200)
	
	user = models.ForeignKey(User, null=True)	

	foursquare_id=models.IntegerField()
	foursquare_token=models.CharField(max_length = 200)
	user_class = models.ForeignKey('UserClass')

	#the players attributes, and the values for them.
	attributes = models.ManyToManyField(Attribute, through='PlayerAttr')

	#also for skills
	skills = models.ManyToManyField(Skill, through='PlayerSkill')

	#and probably inventory as well.
	inventory = models.ManyToManyField('BaseItem', through='PlayerInv')

	#quests
	quests = models.ManyToManyField('Quest', through='PlayerQuest')

	#battles are many-many from player to player - like a friend request
	battles = models.ManyToManyField("self", through='Battle', 
		symmetrical=False)

	#later - perks as a many-many, and race (simple foreign key)

	max_hp = models.IntegerField(default='10') #need to revisit.

	cur_hp = models.IntegerField(default='10') #not sure if this ever gets 
		# used.  probably should go in the battle table.

	exp = models.IntegerField(default='0') #calculate level from this?
	def __unicode__(self):
		return self.player_name
	
    	def is_authenticated(self):
        	"""
	        Always return True. This is a way to tell if the user has been
        	authenticated in templates.
	        """
        	return True

class PlayerSkill (models.Model):
	player = models.ForeignKey('Player')
	skill = models.ForeignKey('Skill')
	level = models.IntegerField() # lack of a record is n/a.

class PlayerInv (models.Model):
	# many to many between players and base items.
	player = models.ForeignKey('Player')
	base_item = models.ForeignKey('BaseItem')

	qty = models.IntegerField() 
	#value?
	#itemName?

	#many to many relationship with modifiers later

class PlayerQuest (models.Model):
	player = models.ForeignKey('Player')
	quest = models.ForeignKey('Quest')

	completed = models.BooleanField()
	#completion date?

class Quest (models.Model):
	quest_name = models.CharField(max_length = 200)
	quest_desc = models.CharField(max_length = 200)
	# later will need quest types, and values for what you need to kill, and 
	# counts of how many you have killed already.


class Battle (models.Model):
	player1 = models.ForeignKey(Player, related_name='attacks')
	u1_hp = models.IntegerField()
	u1_move1 = models.ForeignKey(Skill, related_name='attack_skill')

	player2 = models.ForeignKey(Player, related_name='defends')
	u2_hp = models.IntegerField()
	u2_move1 = models.ForeignKey(Skill, related_name='defend_skill')

	round = models.IntegerField() # prob dont need this, since its not 
		# interactive.
	winner = models.IntegerField() 

	# many to many relationship needed for reward, from battle to items. 
	# calculated at battle time, but needs to be displayed later.
	
	exp_reward = models.IntegerField() #this is calculated at battle, but 
		# needs to be displayed later.  

class ItemType (models.Model):
	item_type_name = models.CharField(max_length = 200)
	
class BaseItem (models.Model):
	base_item_name = models.CharField(max_length = 200)

	item_type = models.ForeignKey(ItemType)
	# subclass baseItem for the major types? weapons, armor, trade goods?
	# so we can have attributes like "min_damage" w/o including that with
	# armor.

class Item (models.Model):
	item_name = models.CharField(max_length = 200) # calculated from the mods
	value = models.IntegerField() #probably calculated
	base_item = models.ForeignKey(BaseItem)
	# maybe like below first, but a many-many with mods is prob better.
	# if there are more than 2, populate the name field differently.
	# prefix = models.ForeignKey(mod) 
	# suffix = models.ForeignKey(mod)

class ItemTypeAttributes (models.Model):
	item_type_attribute_name = models.CharField(max_length = 200)
	# each 	itemType has attributes that apply to it.  these attributes are 
	# populated by the baseItem, and then modified by the mods.
	# eg - Godly Sword of Slaying
	# itemType - weapon
	# this itemType has attributes ranged, a boolean, min dmg, and max dmg
	# the baseItem is "sword" and it has attributes populated for those fields
	# the item itself has a reference to the base item, and the 2 mods

class AttributeType (models.Model):
	#this one is probably overkill.
	attribute_type_name = models.CharField(max_length = 200) # ex - boolean,
		# integer, string(?)

class VenueCategory (models.Model):
	venue_category_name = models.CharField(max_length = 200)
	fs_cat_id = models.IntegerField()

