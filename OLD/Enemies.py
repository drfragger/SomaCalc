from Modifiers import *
import Damage
import Weapons

class Enemy:
	isShielded = False

	def __init__(self, BaseLevel, HPType, BaseHP, ArmorType=None, BaseArmor=0, Level=30):
		self.Level = Level
		self.BaseLevel = BaseLevel
		self.BaseHP = BaseHP
		self.HPType = HPType
		if ArmorType != None:
			self.ArmorType = ArmorType
			self.BaseArmor = BaseArmor
			self.Armor = Damage.EnemyArmorScale(self.BaseArmor, self.Level, self.BaseLevel)

		self.HP = Damage.HealthScale(self.BaseHP, self.Level, self.BaseLevel)

	def EHP(self):
		DMGRedux = (1 - 300 / (300 + self.Armor) )
		rdx = 1 - DMGRedux
		EHP = self.HP / rdx
		if self.isShielded:
			EHP = EHP + self.Shields
			
		return EHP

	def Shielding(self, ShieldType, BaseShields):
		self.isShielded = True
		scale = BaseShields + ((self.Level - self.BaseLevel)**2 * 0.0075 * BaseShields)
		self.ShieldType = ShieldType
		self.Shields = scale

	def printResistances(self):
		for key in Generic.get_dict():
			if hasattr(self, 'Armor'):
				DMM = Damage.ArmorMod(key, self.HPType, self.ArmorType, self.Armor)
				print(key, ":", DMM)
			else:
				selfModif = self.HPType.get_dict()
				print(key, ":", selfModif[key])

	def getResistances(self):
		result = []
		for key in Generic.get_dict():
			if hasattr(self, 'Armor'):
				DMM = Damage.ArmorMod(key, self.HPType, self.ArmorType, self.Armor)
				result.append((key, DMM))
			else:
				selfModif = self.HPType.get_dict()
				result.append((key, selfModif[key]))

		return dict(result)

	def WeakestAgainst(self):
		mydict = self.getResistances()
		maximum = max(mydict, key=mydict.get)
		print(maximum, ":", mydict[maximum])

	def StrongestAgainst(self):
		mydict = self.getResistances()
		minimum = min(mydict, key=mydict.get)
		print(minimum, ":", mydict[minimum])

	def addWeapon(self, Weapon):
		self.Weapon = Weapon
		for key in Generic.get_dict():
			self.Weapon.key = self.Weapon.key * (1 + (self.Level - self.BaseLevel)**1.55 * 0.015)





#Note: Tenno Attributes are Flesh, Ferrite, and Shield.

Lancer = Enemy(1, CFlesh, 100, Ferrite, 100)

CorruptGunner = Enemy(8, CFlesh, 700, Ferrite, 500, Level=100)
CorruptGunner.addWeapon(Weapons.Gorgon)

Teralyst = Enemy(1, Robotic, 100000, Alloy, 300)
Teralyst.Shielding(Shield, 15000)

Charger = Enemy(1, Infested, 80)


#Fun fact: Phorid's armor actually increases incoming corrosive damage up until 2475 armor.
Phorid = Enemy(1, Fossilized, 5000, Ferrite, 25)



CorruptBombard = Enemy(4, CFlesh, 300, Alloy, 500)

JordasGolem = Enemy(1, Sinew, 20000, Ferrite, 250, Level=34)

Juggernaut = Enemy(15, Infested, 3500, Ferrite, 200)

JuggernautBehemoth = Enemy(1, Infested, 4500, Ferrite, 300, Level=500)

TiaMayn = Enemy(1, Flesh, 150, Alloy, 200, Level=85)
TiaMayn.Shielding(Shield, 100)

JenDro = Enemy(1, Flesh, 150, Alloy, 200, Level=85)
JenDro.Shielding(Shield, 100)
