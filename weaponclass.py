


class Weapon:
        
       def __init__(self, name,
                    imp=0, punc=0, sla=0,
                    cld=0, elec=0, ht=0, txn=0,
                    blst=0, crsv=0, gas=0, mag=0,
                    rad=0, vir=0,
                    critC=0.1, critX=2,
                    magazine=60, reload=2, firerate=5, bullets=1):
              
              self.name = name
              
              self.dmg = {'imp': imp, 'punc': punc, 'sla': sla,
                          'cld': cld, 'elec': elec, 'ht': ht, 'txn': txn,
                          'blst': blst, 'crsv': crsv, 'gas': gas, 'mag': mag,
                          'rad': rad, 'vir': vir}
              
              self.stats = {'CritChance': critC, 'Crit Multiplier': critX,
                            'Magazine': magazine, 'Reload': reload, 'Firerate': firerate,
                            'Multishot': bullets}





Braton = Weapon("Braton", imp=7.9, punc=7.9, sla=8.2,
                critC=0.12, critX=1.6, magazine=60,
                firerate=8.75)

Braton.dmg['elec'] = 56
print(Braton.dmg)
                
                    