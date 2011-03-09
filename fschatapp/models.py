from django.db import models

# Create your models here.

class Attribute (models.Model):
	#this class just sets names for attributes.  
	attrName = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.attrName	

class playerAttr (models.Model):
	# many to many relationship, allows setting a player's attrs.
	uAttribute = models.ForeignKey(Attribute)
	player = models.ForeignKey('Player')
	value = models.IntegerField()
	
	#def __unicode__(self):
		#don't want to figure this out just yet, but this should be
		#returning Player:Attribute:Value 
	#	return self.value

class uClass (models.Model):
	verbose_name = "Class"
	verbose_name = "Classes"	

	className = models.CharField(max_length = 200)
	classPrimaryAttr = models.ForeignKey(Attribute, related_name='primary_classes')
	classSecondaryAttr = models.ForeignKey(Attribute, related_name='secondary classes')
	
	def __unicode__(self):
		#later: <classname>: primary - <primary, secondary - <second
		return self.className	

class Skill (models.Model):
	skillName = models.CharField(max_length = 200)
	skillDesc = models.CharField(max_length = 200)
	
	hp_dmg = models.IntegerField()
	mp_dmg = models.IntegerField()
	hp_absorb = models.IntegerField()
	ap_dmg = models.IntegerField()
	
	hp_cost = models.IntegerField()
	mp_cost = models.IntegerField()
	ap_cost = models.IntegerField()

	# later, status effects. blocking isn't possible with this system

	def __unicode__(self):
		return self.skillName	

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
	playerName = models.CharField(max_length = 200)
	playerPassword = models.CharField(max_length = 200)
	foursquareId=models.IntegerField()
	foursquareToken=models.CharField(max_length = 200)
	uClass = models.ForeignKey('uClass')
	#the players attributes, and the values for them.
	attributes = models.ManyToManyField(Attribute, through='playerAttr')

	#also for skills
	skills = models.ManyToManyField(Skill, through='playerSkill')

	#and probably inventory as well.
	inventory = models.ManyToManyField('baseItem', through='playerInv')

	#quests
	quests = models.ManyToManyField('Quest', through='playerQuest')

	#battles are many-many from player to player - like a friend request
	battles = models.ManyToManyField("self", through='Battle', symmetrical=False)

	#later - perks as a many-many, and race (simple foreign key)
	max_hp = models.IntegerField()
	cur_hp = models.IntegerField() #not sure if this ever gets used.  probably should go in the battle table.
	exp = models.IntegerField() #calculate level from this?
	def __unicode__(self):
		return self.playerName	

class playerSkill (models.Model):
	player = models.ForeignKey('Player')
	skill = models.ForeignKey('Skill')
	level = models.IntegerField() # lack of a record is n/a.

class playerInv (models.Model):
	# many to many between players and base items.
	player = models.ForeignKey('Player')
	baseItem = models.ForeignKey('baseItem')

	qty = models.IntegerField() 
	#value?
	#itemName?

	#many to many relationship with modifiers later

class playerQuest (models.Model):
	player = models.ForeignKey('Player')
	quest = models.ForeignKey('Quest')

	completed = models.BooleanField()
	#completion date?

class Quest (models.Model):
	questName = models.CharField(max_length = 200)
	questDesc = models.CharField(max_length = 200)
	#later will need quest types, and values for what you need to kill, and counts of how many you have killed already.


class Battle (models.Model):
	player1 = models.ForeignKey(Player, related_name='attacks')
	u1_hp = models.IntegerField()
	u1_move1 = models.ForeignKey(Skill, related_name='attack_skill')

	player2 = models.ForeignKey(Player, related_name='defends')
	u2_hp = models.IntegerField()
	u2_move1 = models.ForeignKey(Skill, related_name='defend_skill')

	round = models.IntegerField() # prob dont need this, since its not interactive.
	winner = models.IntegerField() 

	# many to many relationship needed for reward, from battle to items. calculated at battle time, but needs to be displayed later.
	
	exp_reward = models.IntegerField() #this is calculated at battle, but needs to be displayed later.  

class itemType (models.Model):
	itemTypeName = models.CharField(max_length = 200)
	
class baseItem (models.Model):
	baseItemName = models.CharField(max_length = 200)

	itemType = models.ForeignKey(itemType)
	# subclass baseItem for the major types? weapons, armor, trade goods?
	# so we can have attributes like "min_damage" w/o including that with
	# armor.

class Item (models.Model):
	itemName = models.CharField(max_length = 200) # calculated from the mods
	value = models.IntegerField() #probably calculated
	baseItem = models.ForeignKey(baseItem)
	# maybe like below first, but a many-many with mods is prob better.
	# if there are more than 2, populate the name field differently.
	# prefix = models.ForeignKey(mod) 
	# suffix = models.ForeignKey(mod)

class itemTypeAttributes (models.Model):
	itemTypeAttributeName = models.CharField(max_length = 200)
	# each 	itemType has attributes that apply to it.  these attributes are 
	# populated by the baseItem, and then modified by the mods.
	# eg - Godly Sword of Slaying
	# itemType - weapon
	# this itemType has attributes ranged, a boolean, min dmg, and max dmg
	# the baseItem is "sword" and it has attributes populated for those fields
	# the item itself has a reference to the base item, and the 2 mods

class attributeType (models.Model):
	#this one is probably overkill.
	attributeTypeName = models.CharField(max_length = 200) # ex - boolean, integer, string(?)

class venueCategory (models.Model):
	venueCategoryName = models.CharField(max_length = 200)
	fsCatId = models.IntegerField()


