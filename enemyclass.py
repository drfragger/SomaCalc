from bodytypes import *
import damagefunctions as df



class Enemy:
    
    def __init__(self, baselevel, hptype, basehp, armortype=Generic, basearmor=0, level=30):
        
        #Props = Properties
        
        self.level = level
        
        self.basetypes = {'hptype': hptype, 'armortype': armortype}
        
        self.baseprops = {'baselevel': baselevel, 'basehp': basehp, 'basearmor': basearmor}
        
        self.props = {'hp': df.health_scaling(self), 'armor': df.armor_scaling(self)}
    
    
    def get_ehp(self):
        
        armor_redux = 1 - (1 - 300 / (300 + self.props['armor']))
        return self.props['hp'] / armor_redux







