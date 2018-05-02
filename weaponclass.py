from bodytypes import *
import damagefunctions as df

class Weapon:
        
       def __init__(self, name,
                    imp=0, punc=0, sla=0,
                    cld=0, elec=0, ht=0, txn=0,
                    blst=0, crsv=0, gas=0, mag=0,
                    rad=0, vir=0,
                    critC=0.1, critX=2,
                    magazine=60, reload=2, firerate=5, bullets=1):
              
              self.name = name
              
              self.basedmg = {'imp': imp, 'punc': punc, 'sla': sla,
                          'cld': cld, 'elec': elec, 'ht': ht, 'txn': txn,
                          'blst': blst, 'crsv': crsv, 'gas': gas, 'mag': mag,
                          'rad': rad, 'vir': vir}
              
              
              self.basestats = {'CritC': critC, 'CritX': critX,
                            'Magazine': magazine, 'Reload': reload, 'Firerate': firerate,
                            'Multishot': bullets}
              
              self.dmg = dict(self.basedmg)
              
              self.stats = dict(self.basestats)
       
       def totaldmg(self, isCrit=False, getBase=False):
              
              dmgdict = (self.dmg, self.basedmg)[getBase]
              
              if isCrit:
                     chance = self.stats['CritC'] * 100
                     mult = self.stats['CritX'] - 1
                     percentinc = ((chance * mult) / 100) + 1
                     return (sum(dmgdict.values())) * percentinc
              else:
                     return sum(dmgdict.values())
       
       def applymod(self, build):
              
              if isinstance(build, tuple):
                     org_build = sorted(build, key=lambda x: x.isLast)
                     for mod in org_build:
                            mod.effect(self)
              else:
                     build.effect(self)
       
       def attack(self, entity, isCrit=False):
              
              crocket = (1, self.stats['CritX'])[isCrit]
              
              ret_val = 0
              
              for key in self.dmg:
                     ret_val += df.damage(self.dmg[key], key, entity, crocket)
              
              return ret_val



                     







