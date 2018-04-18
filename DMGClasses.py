from Modifiers import *
from Damage import *
from random import random



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
    CritChance = 0.10
    #Bullets per second
    FireRate = 5
    #Number of bullets fired per shot
    Bullets = 1
    Magazine = 60
    #In seconds
    Reload = 1

    def __init__(self, name):
        self.Name = name

    def get_elements(self):
        result = []
        for attr in dir(self):
            if not attr.startswith(("__", "CritMult", "CritChance", "FireRate", \
                 "Bullets", "Magazine", "Reload", "Name")):
                value = getattr(self, attr)
                if not callable(value):
                    result.append((attr, value))

        return result

    #The important method
    def get_dict(self):
        result = dict(self.get_elements())
        return result

    def printDMG(self):
        for elem in self.get_dict():
            dmgType = getattr(self, elem)
            if dmgType == 0:
                continue
            print(elem, ":", dmgType)

    def getTotalDMG(self, isCrit=False):
        damagedict = self.get_dict()
        if isCrit:
            for key in damagedict:
                damagedict[key] = damagedict[key] * self.CritMult
        damage = sum(damagedict.values())
        return damage

    
    def Attack(self, Enemy, BodyMult=1, isCrit=False):
        
        #Shields are not accounted for because of how little of an effect they have.

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

            
            
    def DPSAgainst(self, theEnemy=None, isCrit=False):

        if theEnemy is not None:
            BurstDPS = returnBurst(theEnemy, isCrit=isCrit)
            SustainedDPS = returnSustained(theEnemy, isCrit=isCrit)
            print("Burst DPS:", BurstDPS)
            print("Sustained DPS:", SustainedDPS)
        
        else:
            BurstDPS = self.getTotalDMG(isCrit=isCrit) * self.Bullets * self.FireRate
            TimeTaken = (self.Magazine / self.FireRate) + self.Reload
            DamageDealt = self.getTotalDMG(isCrit=isCrit) * self.Bullets * self.Magazine
            SustainedDPS = DamageDealt / TimeTaken
            print("Burst DPS: ", BurstDPS)
            print("Sustained DPS:", SustainedDPS)

    def returnBurst(self, theEnemy, isCrit=False):
        BurstDPS = self.Attack(theEnemy, isCrit=isCrit) * self.Bullets * self.FireRate
        return BurstDPS

    def returnSustained(self, theEnemy, isCrit=False):
        TimeTaken = (self.Magazine / self.FireRate) + self.Reload
        DamageDealt = self.Attack(theEnemy, isCrit=isCrit) * self.Bullets * self.Magazine
        SustainedDPS = DamageDealt / TimeTaken
        return SustainedDPS






class Enemy:
    isShielded = False

    def __init__(self, BaseLevel, HPType, BaseHP, ArmorType=None, BaseArmor=0, ShieldType=Generic, BaseShields=0, Level=30):
        self.Level = Level
        self.BaseLevel = BaseLevel
        self.BaseHP = BaseHP
        self.HPType = HPType
        self.ArmorType = Generic
        self.BaseArmor = 0
        self.Armor = 0
        self.ShieldType = ShieldType
        self.BaseShields = BaseShields
        self.Shields = BaseShields + ((self.Level - self.BaseLevel)**2 * 0.0075 * BaseShields)
        
        if ArmorType != None:
            self.ArmorType = ArmorType
            self.BaseArmor = BaseArmor
            self.Armor = EnemyArmorScale(self.BaseArmor, self.Level, self.BaseLevel)
            

        self.HP = HealthScale(self.BaseHP, self.Level, self.BaseLevel)

    def setlevel(self, Level):
        self.Level = Level
        self.Shields = self.BaseShields + ((self.Level - self.BaseLevel)**2 * 0.0075 * self.BaseShields)
        if self.ArmorType is not None:
            self.Armor = EnemyArmorScale(self.BaseArmor, self.Level, self.BaseLevel)

    def EHP(self):
        DMGRedux = (1 - 300 / (300 + self.Armor) )
        rdx = 1 - DMGRedux
        EHP = self.HP / rdx
        EHP = EHP + self.Shields
            
        return EHP

    def printResistances(self):
        for key in Generic.get_dict():
            if hasattr(self, 'Armor'):
                DMM = ArmorMod(key, self.HPType, self.ArmorType, self.Armor)
                print(key, ":", DMM)
            else:
                selfModif = self.HPType.get_dict()
                print(key, ":", selfModif[key])

    def getResistances(self):
        result = []
        for key in Generic.get_dict():
            if hasattr(self, 'Armor'):
                DMM = ArmorMod(key, self.HPType, self.ArmorType, self.Armor)
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

    def addWeapon(self, theWeapon):
        self.DMG = {}
        etc = theWeapon.get_dict()
        for key in etc:
            self.DMG[key] = etc[key] * (1 + (self.Level - self.BaseLevel)**1.55 * 0.015)

    def Armorize(self, ArmorType, BaseArmor, Level=30):
        self.ArmorType = ArmorType
        self.BaseArmor = BaseArmor
        self.Armor = EnemyArmorScale(self.BaseArmor, self.BaseLevel, self.Level)