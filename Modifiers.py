
class Body:
	#Resistances. More specifically, multipliers.
	Imp = 1
	Punc = 1
	Sla = 1
	Cld = 1
	Elec = 1
	Ht = 1
	Txn = 1
	Blst = 1
	Crsv = 1
	Gas = 1
	Mag = 1
	Rad = 1
	Vir = 1
	Finisher = 1

	def __init__(self, name):
		self.name = name

	def get_elements(self):
		result = []
		for attr in dir(self):
			if not attr.startswith(("__", "name")):
				value = getattr(self, attr)
				if not callable(value):
					result.append((attr, value))

		return result

	def get_dict(self):
		result = dict(self.get_elements())
		return result

	
Imp = "Imp"
Punc = "Punc"
Sla = "Sla"
Cld = "Cld"
Elec = "Elec"
Ht = "Ht"
Txn = "Txn"
Blst = "Blst"
Crsv = "Crsv"
Gas = "Gas"
Mag = "Mag"
Rad = "Rad"
Vir = "Vir"
Finisher = "Finisher"


Generic = Body("Generic")


CFlesh = Body("CFlesh")
CFlesh.Imp = 0.75
CFlesh.Sla = 1.25
CFlesh.Ht = 1.25
CFlesh.Gas = 0.5
CFlesh.Vir = 1.75

#Note: Armor type
Ferrite = Body("Ferrite")
Ferrite.Punc = 1.5
Ferrite.Sla = 0.85
Ferrite.Txn = 1.25
Ferrite.Blst = 0.75
Ferrite.Crsv = 1.75

#Note: Armor type
Alloy = Body("Alloy")
Alloy.Punc = 1.15
Alloy.Sla = 0.5
Alloy.Cld = 1.25
Alloy.Elec = 0.5
Alloy.Mag = 0.5
Alloy.Rad = 1.75

Machinery = Body("Machinery")
Machinery.Imp = 1.25
Machinery.Elec = 1.5
Machinery.Txn = 0.75
Machinery.Blst = 1.75
Machinery.Vir = 0.75

Flesh = Body("Flesh")
Flesh.Imp = 0.75
Flesh.Sla = 1.25
Flesh.Txn = 1.5
Flesh.Gas = 0.75
Flesh.Vir = 1.5

Shield = Body("Shield")
Shield.Imp = 1.5
Shield.Punc = 0.8
Shield.Cld = 1.5
Shield.Txn = 0
Shield.Mag = 1.75
Shield.Rad = 0.75

PShield = Body("PShield")
PShield.Imp = 1.15
PShield.Punc = 0.5
PShield.Ht = 0.5
PShield.Txn = 0
PShield.Crsv = 0.5
PShield.Mag = 1.75

Robotic = Body("Robotic")
Robotic.Punc = 1.25
Robotic.Sla = 0.75
Robotic.Elec = 1.5
Robotic.Txn = 0.75
Robotic.Rad = 1.25

Infested = Body("Infested")
Infested.Sla = 1.25
Infested.Ht = 1.25
Infested.Gas = 1.75
Infested.Rad = 0.5
Infested.Vir = 0.5

IFlesh = Body("IFlesh")
IFlesh.Sla = 1.5
IFlesh.Cld = 0.5
IFlesh.Ht = 1.5
IFlesh.Gas = 1.5

Fossilized = Body("Fossilized")
Fossilized.Sla = 1.15
Fossilized.Cld = 0.75
Fossilized.Txn = 0.5
Fossilized.Blst = 1.5
Fossilized.Crsv = 1.75
Fossilized.Rad = 0.75

Sinew = Body("Sinew")
Sinew.Punc = 1.25
Sinew.Cld = 1.25
Sinew.Blst = 0.5
Sinew.Rad = 1.5
Sinew.Finisher = 1.33




