from wf_class_defs import Enemy
import bodytypes

types = bodytypes.init()

'''
Used to create and store enemy objects for use in the application.
If there are some enemy variants missing, it is because they are identical to
the original. Nightwatch falls under this catagory.

Prefixes:
O = Orokin (Corrupted)
G = Grineer
D = Drekar (Uranus)
K = Kuva
T = Tusk (Plains)
A = Arid
F = Frontier
C = Corpus
I = Infested
M = Mutalist
S = Sentient
'''

################## Corrupted (Orokin) Enemies ################

O_LANCER = Enemy("O_LANCER", 1, types['CFlesh'], 60, types['Alloy'], 200)

O_BUTCHER = Enemy("O_BUTCHER", 1, types['CFlesh'], 100, types['Ferrite'], 5)

O_CREWMAN = Enemy("O_CREWMAN", 1, types['Shield'], 150)

O_NULLIFIER = Enemy("O_NULLIFIER", 15, types['PShield'], 150)

O_DRONE = Enemy("O_DRONE", 1, types['Shield'], 50)

O_HEAVY_GUNNER = Enemy("O_HEAVY_GUNNER", 8, types['CFlesh'], 700, types['Ferrite'], 500)

O_BOMBARD = Enemy("O_BOMBARD", 4, types['CFlesh'], 300, types['Alloy'], 500)

O_MOA = Enemy("O_MOA", 1, types['Shield'], 250)

O_MOA_DRONE = Enemy("O_MOA_DRONE", 1, types['Shield'], 75)

O_ANCIENT = Enemy("O_ANCIENT", 1, types['Fossil'], 400)


corrupt_temp = [O_LANCER, O_BUTCHER, O_CREWMAN, O_NULLIFIER, \
                   O_DRONE, O_HEAVY_GUNNER, O_BOMBARD, O_MOA, \
                   O_MOA_DRONE, O_ANCIENT]

corrupt_enemies = {x.name: x for x in corrupt_temp}

##############################################################



#################### Grineer Enemies #########################

G_BUTCHER = Enemy("G_BUTCHER", 1, types['CFlesh'], 50, types['Ferrite'], 5)

G_FLAMEBLADE = Enemy("G_FLAMEBLADE", 3, types['CFlesh'], 50, types['Ferrite'], 5)

G_GUARDSMAN = Enemy("G_GUARDSMAN", 1, types['CFlesh'], 150, types['Ferrite'], 5)

G_POWERFIST = Enemy("G_POWERFIST", 5, types['CFlesh'], 100, types['Ferrite'], 5)
T_PREDATOR = Enemy("T_PREDATOR", 5, types['CFlesh'], 75, types['Ferrite'], 5)

G_SCORPION = Enemy("G_SCORPION", 10, types['CFlesh'], 150, types['Ferrite'], 150)
D_SCORPION = Enemy("D_SCORPION", 1, types['CFlesh'], 350, types['Ferrite'], 150)

G_SHIELD_LANCER = Enemy("G_SHIELD_LANCER", 5, types['CFlesh'], 100, types['Ferrite'], 5)



G_BALLISTA = Enemy("G_BALLISTA", 1, types['CFlesh'], 100, types['Ferrite'], 100)

G_ELITE_LANCER = Enemy("G_ELITE_LANCER", 15, types['CFlesh'], 150, types['Alloy'], 200)
A_ELITE_LANCER = Enemy("A_ELITE_LANCER", 10, types['CFlesh'], 150, types['Alloy'], 200)

G_EVISCERATOR = Enemy("G_EVISCERATOR", 15, types['CFlesh'], 150, types['Alloy'], 200)

G_HELLION = Enemy("G_HELLION", 15, types['CFlesh'], 100, types['Ferrite'], 100)
A_HELLION = Enemy("A_HELLION", 1, types['CFlesh'], 180, types['Ferrite'], 100)

G_LANCER = Enemy("G_LANCER", 1, types['CFlesh'], 100, types['Ferrite'], 100)

G_SCORCH = Enemy("G_SCORCH", 10, types['CFlesh'], 120, types['Ferrite'], 100)

G_SEEKER = Enemy("G_SEEKER", 1, types['CFlesh'], 100, types['Ferrite'], 200)

G_TROOPER = Enemy("G_TROOPER", 1, types['CFlesh'], 120, types['Ferrite'], 150)
A_TROOPER = Enemy("A_TROOPER", 1, types['CFlesh'], 120, types['Ferrite'], 100)
F_TROOPER = Enemy("F_TROOPER", 1, types['CFlesh'], 65, types['Ferrite'], 100)
D_TROOPER = Enemy("D_TROOPER", 1, types['CFlesh'], 120, types['Ferrite'], 100)



G_BAILIFF = Enemy("G_BAILIFF", 1, types['CFlesh'], 700, types['Alloy'], 500)
T_REAVER = Enemy("T_REAVER", 1, types['CFlesh'], 200, types['Ferrite'], 500)

G_BOMBARD = Enemy("G_BOMBARD", 4, types['CFlesh'], 300, types['Alloy'], 500)

G_COMMANDER = Enemy("G_COMMANDER", 3, types['CFlesh'], 500, types['Ferrite'], 95)

G_DRAHK_MASTER = Enemy("G_DRAHK_MASTER", 12, types['CFlesh'], 500, types['Ferrite'], 200)

G_HEAVY_GUNNER = Enemy("G_HEAVY_GUNNER", 8, types['CFlesh'], 300, types['Ferrite'], 500)
F_HEAVY_GUNNER = Enemy("F_HEAVY_GUNNER", 8, types['CFlesh'], 350, types['Ferrite'], 500)

G_HYEKKA_MASTER = Enemy("G_HYEKKA_MASTER", 1, types['CFlesh'], 650, types['Ferrite'], 50)

G_MANIC = Enemy("G_MANIC", 1, types['CFlesh'], 350, types['Ferrite'], 25)
D_MANIC = Enemy("D_MANIC", 1, types['CFlesh'], 450, types['Ferrite'], 25)

G_NAPALM = Enemy("G_NAPALM", 6, types['CFlesh'], 600, types['Alloy'], 500)
T_NAPALM = Enemy("T_NAPALM", 6, types['CFlesh'], 450, types['Alloy'], 500)

G_NOX = Enemy("G_NOX", 1, types['CFlesh'], 350, types['Alloy'], 250)

G_DRAHK = Enemy("G_DRAHK", 1, types['Flesh'], 300, types['Ferrite'], 175)

G_HYEKKA = Enemy("G_HYEKKA", 1, types['Flesh'], 300, types['Ferrite'], 175)


grineer_temp = [G_BUTCHER, G_FLAMEBLADE, G_GUARDSMAN, G_POWERFIST, \
                T_PREDATOR, G_SCORPION, D_SCORPION, G_SHIELD_LANCER, \
                G_BALLISTA, G_ELITE_LANCER, A_ELITE_LANCER, G_EVISCERATOR, \
                G_HELLION, A_HELLION, G_LANCER, G_SCORCH, \
                G_SEEKER, G_TROOPER, A_TROOPER, F_TROOPER, \
                D_TROOPER, G_BAILIFF, T_REAVER, G_BOMBARD, \
                G_COMMANDER, G_DRAHK_MASTER, G_HEAVY_GUNNER, F_HEAVY_GUNNER, \
                G_HYEKKA_MASTER, G_MANIC, D_MANIC, G_NAPALM, \
                T_NAPALM, G_NOX, G_DRAHK, G_HYEKKA]

grineer_enemies = {x.name: x for x in grineer_temp}

##############################################################



################ Corpus Enemies ##############################

C_COMBA = (Enemy("C_COMBA", 15, types['Shield'], 400), 
           Enemy("C_COMBA", 15, types['Flesh'], 1100))

C_CREWMAN = (Enemy("C_CREWMAN", 1, types['Shield'], 150), 
             Enemy("C_CREWMAN", 1, types['Flesh'], 60))

C_DETRON_CREWMAN = (Enemy("C_DETRON_CREWMAN", 1, types['Shield'], 150), 
                    Enemy("C_DETRON_CREWMAN", 1, types['Flesh'], 60))

C_ELITE_CREWMAN = (Enemy("C_ELITE_CREWMAN", 15, types['Shield'], 200),
                   Enemy("C_ELITE_CREWMAN", 15, types['Flesh'], 100))

C_NULLIFIER = (Enemy("C_NULLIFIER", 15, types['PShield'], 150),
               Enemy("C_NULLIFIER", 15, types['Flesh'], 60))

C_PRODMAN = (Enemy("C_PRODMAN", 1, types['Shield'], 50),
             Enemy("C_PRODMAN", 1, types['Flesh'], 100))

C_SCRAMBUS = (Enemy("C_SCRAMBUS", 15, types['Shield'], 400),
              Enemy("C_SCRAMBUS", 15, types['Flesh'], 1100))

C_SNIPER_CREWMAN = (Enemy("C_SNIPER_CREWMAN", 15, types['PShield'], 150),
                    Enemy("C_SNIPER_CREWMAN", 15, types['Flesh'], 60))

C_TECH = (Enemy("C_TECH", 15, types['PShield'], 250),
          Enemy("C_TECH", 15, types['Flesh'], 700))



C_ANTI_MOA = (Enemy("C_ANTI_MOA", 1, types['Shield'], 500),
              Enemy("C_ANTI_MOA", 1, types['Robotic'], 50))

C_DENIAL_BURSA = (Enemy("C_DENIAL_BURSA", 1, types['Shield'], 700),
                  Enemy("C_DENIAL_BURSA", 1, types['Robotic'], 1200))

# Note: Drover and Isolator Bursas are functionally identical.
C_DROVER_BURSA = (Enemy("C_DROVER_BURSA", 1, types['Shield'], 700),
                  Enemy("C_DROVER_BURSA", 1, types['Robotic'], 1200, types['Alloy'], 200))

C_FUSION_MOA = (Enemy("C_FUSION_MOA", 10, types['Shield'], 250),
                Enemy("C_FUSION_MOA", 10, types['Robotic'], 250))

C_MOA = (Enemy("C_MOA", 1, types['Shield'], 150),
         Enemy("C_MOA", 1, types['Robotic'], 60))
C_SHOCKWAVE_MOA = (Enemy("C_SHOCKWAVE_MOA", 5, types['Shield'], 150),
                   Enemy("C_SHOCKWAVE_MOA", 5, types['Robotic'], 60))

C_ATTACK_DRONE = (Enemy("C_ATTACK_DRONE", 1, types['Shield'], 75),
                  Enemy("C_ATTACK_DRONE", 1, types['Robotic'], 250))

C_LEECH_OSPREY = (Enemy("C_LEECH_OSPREY", 15, types['Shield'], 50),
                  Enemy("C_LEECH_OSPREY", 15, types['Robotic'], 100))

C_LYNX_OSPREY = (Enemy("C_LYNX_OSPREY", 1, types['Shield'], 50),
                 Enemy("C_LYNX_OSPREY", 1, types['Robotic'], 35))

C_MINE_OSPREY = (Enemy("C_MINE_OSPREY", 10, types['Shield'], 50),
                 Enemy("C_MINE_OSPREY", 10, types['Robotic'], 100))

C_OXIUM_OSPREY = (Enemy("C_OXIUM_OSPREY", 5, types['Shield'], 150),
                  Enemy("C_OXIUM_OSPREY", 5, types['Robotic'], 750, types['Ferrite'], 40))

C_SCAVENGER_DRONE = (Enemy("C_SCAVENGER_DRONE", 1, types['Shield'], 50),
                     Enemy("C_SCAVENGER_DRONE", 1, types['Robotic'], 100))

C_SAPPING_OSPREY = (Enemy("C_SAPPING_OSPREY", 1, types['Shield'], 50),
                    Enemy("C_SAPPING_OSPREY", 1, types['Robotic'], 200))

C_SHIELD_OSPREY = (Enemy("C_SHIELD_OSPREY", 1, types['Shield'], 50),
                   Enemy("C_SHIELD_OSPREY", 1, types['Robotic'], 35))

C_RATEL = (Enemy("C_RATEL", 1, types['PShield'], 30),
           Enemy("C_RATEL", 1, types['Robotic'], 10))


corpus_temp = [C_COMBA, C_CREWMAN, C_DETRON_CREWMAN, C_ELITE_CREWMAN, \
               C_NULLIFIER, C_PRODMAN, C_SCRAMBUS, C_SNIPER_CREWMAN, \
               C_TECH, C_ANTI_MOA, C_DENIAL_BURSA, C_DROVER_BURSA, \
               C_FUSION_MOA, C_MOA, C_SHOCKWAVE_MOA, C_ATTACK_DRONE, \
               C_LEECH_OSPREY, C_LYNX_OSPREY, C_MINE_OSPREY, C_OXIUM_OSPREY, \
               C_SCAVENGER_DRONE, C_SAPPING_OSPREY, C_SHIELD_OSPREY, C_RATEL]

corpus_enemies = {x[0].name: x for x in corpus_temp}

##############################################################



##################### Infested Enemies #######################

I_CHARGER = Enemy("I_CHARGER", 1, types['Infested'], 80)

I_LEAPER = Enemy("I_LEAPER", 1, types['Infested'], 100)

I_MAGGOT = Enemy("I_MAGGOT", 1, types['Infested'], 20)

I_VOLATILE_RUNNER = Enemy("I_VOLATILE_RUNNER", 1, types['IFlesh'], 80)

I_CRAWLER = Enemy("I_CRAWLER", 1, types['IFlesh'], 50)



M_OSPREY = Enemy("M_OSPREY", 1, types['IFlesh'], 200)

M_SWARM_MOA = Enemy("M_SWARM_MOA", 12, types['Fossil'], 350)



I_ANCIENT_DISRUPTOR = Enemy("I_ANCIENT_DISRUPTOR", 1, types['Fossil'], 400)

I_BOILER = Enemy("I_BOILER", 12, types['Fossil'], 1200)
I_ARCANE_BOILER = Enemy("I_ARCANE_BOILER", 12, types['Fossil'], 2200)

I_BROOD_MOTHER = Enemy("I_BROOD_MOTHER", 12, types['Fossil'], 700)

I_JUGGERNAUT = Enemy("I_JUGGERNAUT", 15, types['Infested'], 3500, types['Ferrite'], 200)

I_JUGGERNAUT_BEHEMOTH = Enemy("I_JUGGERNAUT_BEHEMOTH", 15, types['Infested'], 4500, types['Ferrite'], 300)

I_PHORID = Enemy("I_PHORID", 1, types['Fossil'], 5000, types['Ferrite'], 25)


infested_temp = [I_CHARGER, I_LEAPER, I_MAGGOT, I_VOLATILE_RUNNER, \
                 I_CRAWLER, M_OSPREY, M_SWARM_MOA, I_ANCIENT_DISRUPTOR, \
                 I_BOILER, I_ARCANE_BOILER, I_BROOD_MOTHER, I_JUGGERNAUT, \
                 I_JUGGERNAUT_BEHEMOTH, I_PHORID]

infested_enemies = {x.name: x for x in infested_temp}

##############################################################



######################### Sentient Enemies ###################

S_BATTALYST = Enemy("S_BATTALYST", 1, types['Robotic'], 1300, types['Ferrite'], 250)

S_CONCULYST = Enemy("S_CONCULYST", 1, types['Robotic'], 1300, types['Ferrite'], 250)

S_OCULYST = Enemy("S_OCULYST", 1, types['Robotic'], 300, types['Ferrite'], 150)

S_VOMVALYST = Enemy("S_VOMVALYST", 1, types['Robotic'], 700)

S_TERALYST = (Enemy("S_TERALYST", 1, types['Shield'], 2500), 
              Enemy("S_TERALYST", 1, types['Robotic'], 15000, types['Alloy'], 200))


sentient_temp = [S_BATTALYST, S_CONCULYST, S_OCULYST, S_VOMVALYST]

sentient_enemies = {x.name: x for x in sentient_temp}
sentient_enemies.update({S_TERALYST[0].name: S_TERALYST})

##############################################################


def init():
  all_enemies = {}
  all_enemies.update(corrupt_enemies)
  all_enemies.update(grineer_enemies)
  all_enemies.update(corpus_enemies)
  all_enemies.update(infested_enemies)
  all_enemies.update(sentient_enemies)
  return all_enemies






