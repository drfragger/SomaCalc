from bodytypes import *

class Mod:
    
    def __init__(self, modtype, stat, bonus):
        validtypes = ['damage', 'other']
        assert modtype in validtypes, "Invalid mod type."
        
        self.modtype = modtype
        self.stat = stat
        self.bonus = bonus
        
        self.isLast = (0, 1)[self.stat == 'All']
        
        
    def effect(self, weapon_arg):
        if self.modtype == 'damage':
            
            if self.stat != 'All':
                
                isStatZero = weapon_arg.basedmg[self.stat] == 0
                
                zerostat = weapon_arg.totaldmg(getBase=True) * self.bonus
                
                nonzerostat = (weapon_arg.basedmg[self.stat] * (1 + self.bonus)) - weapon_arg.basedmg[self.stat]
                
                weapon_arg.dmg[self.stat] += (nonzerostat, zerostat)[isStatZero]
            
            else:
                for elem in weapon_arg.dmg:
                    weapon_arg.dmg[elem] *= (1 + self.bonus)
        
        if self.modtype == 'other':
            weapon_arg.stats[self.stat] += weapon_arg.basestats[self.stat] * self.bonus





Dummy = Mod('damage', 'All', 0)

Serration = Mod('damage', 'All', 1.65)
FangedFusillade = Mod('damage', 'sla', 1.2)

HighVoltage = Mod('damage', 'elec', 0.6)
SawtoothClip = Mod('damage', 'sla', 0.3)

Stormbringer = Mod('damage', 'elec', 0.9)
InfectedClip = Mod('damage', 'txn', 0.9)
Hellfire = Mod('damage', 'ht', 0.9)
CryoRounds = Mod('damage', 'cld', 0.9)



SpeedTrigger = Mod('other', 'Firerate', 0.6)
Shred = Mod('other', 'Firerate', 0.3)
                

