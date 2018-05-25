from bodytypes import *
import damagefunctions as df



class Enemy:
    
    def __init__(self, name, baselevel, hptype, basehp, armortype=Generic, basearmor=0, level=30):
        '''
        IMPORTANT NOTE: Shielded enemies should use a shield type for their HP type.
        '''
        
        #Props = Properties
        
        self.name = name
        
        self.level = level
        
        self.basetypes = {'hptype': hptype, 'armortype': armortype}
        
        self.baseprops = {'baselevel': baselevel, 'basehp': basehp, 'basearmor': basearmor}
        
        self.props = {'hp': df.health_scaling(self), 'armor': df.armor_scaling(self)}
    
    @property
    def ehp(self):
        armor_redux = 1 - (1 - 300 / (300 + self.props['armor']))
        return self.props['hp'] / armor_redux
    
    def get_resistances(self):
        entity_resistances = []
        
        for elem in Generic._fields:
            el_res = df.damage_mitigation(elem, self)
            entity_resistances.append((elem, el_res))
        
        return dict(entity_resistances)
    
    def __repr__(self):
        return self.name
        
        







