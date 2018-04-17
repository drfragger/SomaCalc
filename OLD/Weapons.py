from Modifiers import *
from Damage import *
from Enemies import *

class Weapon:
	#TODO: Add Crit stats and status chance
	Imp = 0
	Punc = 0
	Sla = 0
	Cld = 0
	Elec = 0
	Ht = 0
	Txn = 0
	Blst = 0
	Crsv = 0
	Gas = 0
	Mag = 0
	Rad = 0
	Vir = 0
	CritMult = 2


	def get_elements(self):
		result = []
		for attr in dir(self):
			if not attr.startswith(("__", "CritMult")):
				value = getattr(self, attr)
				if not callable(value):
					result.append((attr, value))

		return result

	#The important method
	def get_dict(self):
		result = dict(self.get_elements())
		return result

	def DealRawDMG(self, Enemy, BodyMult=1, isCrit=False):
		if isCrit:
			Crocket = self.CritMult
		else:
			Crocket = 1

		result = 0
		res = dict(self.get_dict())
		for key in res:
			result += NoArmorDMG(res[key], key, Enemy.HPType, Crocket, BodyMult)

		return result

	def DealArmorDMG(self, Enemy, BodyMult=1, isCrit=False):
		if isCrit:
			Crocket = self.CritMult
		else:
			Crocket = 1

		result = 0
		res = dict(self.get_dict())
		for key in res:

			Redux = ArmorMod(key, Enemy.HPType, Enemy.ArmorType, Enemy.Armor, Crocket, BodyMult)
			result += ArmorDMG(res[key], Redux)

		return result




Braton = Weapon()
Braton.Imp = 18.365
Braton.Punc = 18.365
Braton.Sla = 18.921
Braton.Crsv = 107.9


Aeger = Weapon()
Aeger.Imp = 59.070
Aeger.Punc = 148.184
Aeger.Sla = 88.605
Aeger.Vir = 118.649
Aeger.Crsv = 497.410

Opticor = Weapon()
Opticor.Imp = 2655.25
Opticor.Punc = 49653.175
Opticor.Sla = 1327.625
Opticor.Rad = 47794.5
Opticor.CritMult = 5.5

Gorgon = Weapon()
Gorgon.Imp = 18.75
Gorgon.Punc = 3.75
Gorgon.Sla = 2.5
Gorgon.CritMult = 1.5