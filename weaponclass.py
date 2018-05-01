import modclass as mc


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
              
              self.dmg = dict(self.basedmg)
              
              self.stats = {'CritC': critC, 'CritX': critX,
                            'Magazine': magazine, 'Reload': reload, 'Firerate': firerate,
                            'Multishot': bullets}
       
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
              
              org_build = sorted(build, key=lambda x: x.isLast)
              for mod in org_build:
                     mod.effect(self)
                     




mybuild = (mc.Serration, mc.FangedFusillade, mc.SawtoothClip, mc.Stormbringer, mc.HighVoltage)


Braton = Weapon("Braton", imp=7.9, punc=7.9, sla=8.2,
                critC=0.12, critX=1.6, magazine=60,
                firerate=8.75)

Braton.applymod(mybuild)


for x in Braton.dmg:
       if Braton.dmg[x] != 0:
              print(f'{x}: {Braton.dmg[x]}')