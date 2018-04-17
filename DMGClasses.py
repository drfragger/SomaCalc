from Modifiers import *
from Damage import *
from ModClass import Mod
from RandoMethods import most_common
from RandoMethods import weighted_random_by_dct as wrand
from random import random
import math



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
    StatusChance = 0.15
    BaseBullets = 1

    def __init__(self, name):
        self.Name = name

    def get_elements(self):
        result = []
        for attr in dir(self):
            if not attr.startswith(("__", "CritMult", "CritChance", "FireRate", \
                 "Bullets", "Magazine", "Reload", "Name", "StatusChance", "BaseBullets")):
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

    
    def Attack(self, Enemy, BodyMult=1, isCrit=False, includeProcs=False):
        
        ##Shields are not accounted for because of how little of an effect they have.

        randgen = random()

        ProcDMG = 0

        if includeProcs == True:

            if randgen <= self.StatusChance:
                ProcDict = self.PropProcChance()
                ProcList = []
                for i in range(100):
                    ProcList.insert(0, wrand(ProcDict))

                WhatProcced = most_common(ProcList)

                for i in range(math.floor(self.Bullets)):
                
                    if WhatProcced == 'Sla':
                        ProcDMG += self.SlashProc()

                    if WhatProcced == 'Txn':
                        ProcDMG += self.ToxinProc(Enemy)

                    if WhatProcced == 'Ht':
                        ProcDMG += self.HeatProc(Enemy)

                    if WhatProcced == 'Vir':
                        self.ViralProc(Enemy)

                    #if WhatProcced == 'Crsv':
                        #self.CorrosiveProc(Enemy)


        if isCrit:
            Crocket = self.CritMult
        else:
            Crocket = 1

        result = 0
        res = dict(self.get_dict())
        for key in res:

            Redux = ArmorMod(key, Enemy.HPType, Enemy.ArmorType, Enemy.Armor, Crocket, BodyMult)
            result += ArmorDMG(res[key], Redux) + ProcDMG

        return result

    
    def PowerUp(self, *themods):
        Build = sorted(themods, key=lambda x: x.priority)
        for mod in Build:
            mod.modify(self)
            
            

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

    def ChancePerPellet(self):
        CPP = 1 - (1 - self.StatusChance)**(1 / self.BaseBullets)
        return CPP

    def ProcsTriggered(self):
        procs = self.Bullets * self.ChancePerPellet()
        return procs
    
    def PropProcChance(self):
        TotalPDamage = 0
        ProcDict = self.get_dict()
        ProcDict = dict.fromkeys(ProcDict, 0)

        for elem in self.get_dict():
            DMGType = getattr(self, elem)
            if elem in ('Imp', 'Punc', 'Sla'):
                DMGType *= 4

            TotalPDamage += DMGType

        for elem in self.get_dict():
            DMGType = getattr(self, elem)
            if elem in ('Imp', 'Punc', 'Sla'):
                DMGType *= 4

            ProcDict[elem] = DMGType / TotalPDamage

        return ProcDict

    def SlashProc(self):
        ProcDMG = self.getTotalDMG() * 0.35
        ContinuousProcs = ProcDMG * 7
        return ContinuousProcs

    def ToxinProc(self, Enemy):
        ToxProcDMG = (self.Txn + self.getTotalDMG()) / 2
        ToxinProcOverTime = ToxProcDMG * 9
        LocalMod = ArmorMod(Txn, Enemy.HPType, Enemy.ArmorType, Enemy.Armor)
        return ArmorDMG(ToxinProcOverTime, LocalMod)

    def HeatProc(self, Enemy):
        HeatProcDMG = (self.Ht + self.getTotalDMG()) / 2
        HeatProcOverTime = HeatProcDMG * 7
        LocalMod = ArmorMod(Ht, Enemy.HPType, Enemy.ArmorType, Enemy.Armor)
        return ArmorDMG(HeatProcOverTime, LocalMod)

    def ViralProc(self, Enemy):
        if not Enemy.hasViral:
            Enemy.HP = Enemy.HP / 2
            Enemy.hasViral = True

    def CorrosiveProc(self, Enemy):
        Enemy.Armor = Enemy.Armor - (Enemy.Armor * 0.25)

    def detectDualStat(self):
        pass









class Enemy:
    isShielded = False
    hasViral = False

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