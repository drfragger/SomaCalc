from bodytypes import *
import damagefunctions as df

class Weapon:
        
       def __init__(self, name,
                    imp=0, punc=0, sla=0,
                    cld=0, elec=0, ht=0, txn=0,
                    blst=0, crsv=0, gas=0, mag=0,
                    rad=0, vir=0,
                    critC=0.1, critX=2,
                    magazine=60, reload=2, firerate=5, bullets=1,
                    chargetime=0):
              
              self.name = name
              
              self.basedmg = {'imp': imp, 'punc': punc, 'sla': sla,
                          'cld': cld, 'elec': elec, 'ht': ht, 'txn': txn,
                          'blst': blst, 'crsv': crsv, 'gas': gas, 'mag': mag,
                          'rad': rad, 'vir': vir}
              
              
              self.basestats = {'CritC': critC, 'CritX': critX,
                            'Magazine': magazine, 'Reload': reload,
                            'Firerate': firerate, 'Multishot': bullets,
                            'Charge Time': chargetime}
              
              
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
                            self.update_elemental_combos()
              else:
                     build.effect(self)
                     self.update_elemental_combos()
       
       def attack(self, entity, isCrit=False):
              
              crocket = (1, self.stats['CritX'])[isCrit]
              
              ret_val = 0
              
              for key in self.dmg:
                     ret_val += df.damage(self.dmg[key], key, entity, crocket)
              
              return ret_val
       
       
       def get_dps(self, isCrit=False):
              
              real_fire_rate = self.stats['Firerate'] / (1 + self.stats['Charge Time'])
              
              if self.stats['Firerate'] == 0:
                     real_fire_rate = 1 / self.stats['Charge Time']
       
              burst = self.totaldmg(isCrit=isCrit) * self.stats['Multishot'] * real_fire_rate
              
              time_elapsed = (self.stats['Magazine'] / real_fire_rate) + self.stats['Reload']
              sus_dmg_dealt = self.totaldmg(isCrit=isCrit) * self.stats['Multishot'] * self.stats['Magazine']
              sustained = sus_dmg_dealt / time_elapsed
              
              return (burst, sustained)
              
              
       
       
       
       def get_sustained(self, victim, isCrit=False):
              
              real_fire_rate = self.stats['Firerate'] / (1 + self.stats['Charge Time'])
              
              if self.stats['Firerate'] == 0:
                     real_fire_rate = 1 / self.stats['Charge Time']              
              
              time_elapsed = (self.stats['Magazine'] / real_fire_rate) + self.stats['Reload']
              damage_dealt = self.attack(victim, isCrit) * self.stats['Multishot'] * self.stats['Magazine']
              sustained = damage_dealt / time_elapsed
              return sustained
       
       
       def get_burst(self, victim, isCrit=False):
              
              real_fire_rate = self.stats['Firerate'] / (1 + self.stats['Charge Time'])
              
              if self.stats['Firerate'] == 0:
                     real_fire_rate = 1 / self.stats['Charge Time']
              
              burst = self.attack(victim, isCrit) * self.stats['Multishot'] * real_fire_rate
              return burst
       
       
       def update_elemental_combos(self):
              
              blst_check = bool(self.dmg['blst'] or (self.dmg['ht'] and self.dmg['cld']))
              crsv_check = bool(self.dmg['crsv'] or (self.dmg['txn'] and self.dmg['elec']))
              gas_check = bool(self.dmg['gas'] or (self.dmg['txn'] and self.dmg['ht']))
              mag_check = bool(self.dmg['mag'] or (self.dmg['cld'] and self.dmg['elec']))
              rad_check = bool(self.dmg['rad'] or (self.dmg['ht'] and self.dmg['elec']))
              vir_check = bool(self.dmg['vir'] or (self.dmg['cld'] and self.dmg['txn']))
              
              if blst_check:
                     self.dmg['blst'] += self.dmg['ht'] + self.dmg['cld']
                     self.dmg['ht'], self.dmg['cld'] = 0, 0
              
              if crsv_check:
                     self.dmg['crsv'] += self.dmg['txn'] + self.dmg['elec']
                     self.dmg['txn'], self.dmg['elec'] = 0, 0
              
              if gas_check:
                     self.dmg['gas'] += self.dmg['ht'] + self.dmg['txn']
                     self.dmg['ht'], self.dmg['txn'] = 0, 0  
              
              if mag_check:
                     self.dmg['mag'] += self.dmg['cld'] + self.dmg['elec']
                     self.dmg['elec'], self.dmg['cld'] = 0, 0
              
              if rad_check:
                     self.dmg['rad'] += self.dmg['ht'] + self.dmg['elec']
                     self.dmg['ht'], self.dmg['elec'] = 0, 0
              
              if vir_check:
                     self.dmg['vir'] += self.dmg['txn'] + self.dmg['cld']
                     self.dmg['txn'], self.dmg['cld'] = 0, 0

