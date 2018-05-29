import sys
sys.path.append('..')
from weaponclass import Weapon
import pickle


###################### Primaries #############################################################################


#################### Rifles ##################################

ARGONAK = (Weapon('ARGONAK_AUTO', 24.5, 6.3, 26.2, critC=0.09, critX=1.5,
                  magazine=43, reload=2.4, firerate=6),
           Weapon('ARGONAK_SEMI', 24.5, 6.3, 26.2, critC=0.27, critX=2.3,
                  magazine=43, reload=2.4, firerate=4.33))

BAZA = Weapon('BAZA', 5.8, 6.7, 3.5, critC=0.26, critX=3,
              magazine=40, reload=1.4, firerate=16.67)

BOLTOR = Weapon('BOLTOR', 2.5, 20.0, 2.5, critC=0.1, critX=1.8,
                magazine=60, reload=2.6, firerate=8.75)
BOLTOR_PRIME = Weapon('BOLTOR_PRIME', 4.6, 41.4, sla=0, critC=0.12, critX=2,
                      magazine=60, reload=2.4, firerate=10)
TELOS_BOLTOR = Weapon('TELOS_BOLTOR', 3, 27, sla=0, critC=0.3, critX=2.4,
                      magazine=90, reload=2.4, firerate=9.33)

BRATON = Weapon('BRATON', 7.9, 7.9, 8.2, critC=0.12, critX=1.6,
                magazine=45, reload=2, firerate=8.75)
BRATON_PRIME = Weapon('BRATON_PRIME', 1.75, 12.25, 21.0, critC=0.12, critX=2,
                      magazine=75, reload=2.15, firerate=9.58)
BRATON_VANDAL = Weapon('BRATON_VANDAL', 12.25, 1.75, 21, critC=0.16, critX=2,
                       magazine=50, reload=1.75, firerate=7.5)
MK1_BRATON = Weapon('MK1_BRATON', 4.5, 4.5, 9, critC=0.08, critX=1.5,
                    magazine=60, reload=2, firerate=7.5)

BURSTON = Weapon('BURSTON', 10, 10, 10, critC=0.06, critX=1.6,
                 magazine=45, reload=2, firerate=7.83)
BURSTON_PRIME = Weapon('BURSTON_PRIME', 10.8, 10.8, 14.4, critC=0.18, critX=1.8,
                       magazine=45, reload=2, firerate=13.64)

BUZLOK = Weapon('BUZLOK', 30, 24, 6, critC=0.23, critX=2.5,
                magazine=50, reload=3, firerate=6.25)

DERA = Weapon('DERA', 6, 22.5, 1.5, critC=0.08, critX=1.6,
              magazine=45, reload=1.8, firerate=11.25)
DERA_VANDAL = Weapon('DERA_VANDAL', 6.4, 24, 1.6, critC=0.08, critX=2,
                     magazine=60, reload=1.8, firerate=11.25)

GORGON = Weapon('GORGON', 18.75, 3.75, 2.5, critC=0.17, critX=1.5,
                magazine=90, reload=4.2, firerate=12.5)
PRISMA_GORGON = Weapon('PRISMA_GORGON', 17.3, 3.5, 2.3, critC=0.3, critX=2.3,
                       magazine=120, reload=3, firerate=14.17)
GORGON_WRAITH = Weapon('GORGON_WRAITH', 23, 2.7, 1.3, critC=0.15, critX=1.9,
                       magazine=90, reload=3, firerate=13.3)

GRAKATA = Weapon('GRAKATA', 4.4, 3.7, 2.9, critC=0.25, critX=2,
                 magazine=60, reload=2.4, firerate=20)
PRISMA_GRAKATA = Weapon('PRISMA_GRAKATA', 6, 5, 4, critC=0.25, critX=2.5, 
                        magazine=120, reload=2, firerate=21.67)

GRINLOK = Weapon('GRINLOK', 93.5, 18.7, 74.8, critC=0.15, critX=2.5, 
                 magazine=9, reload=1.7, firerate=1.67)

HARPAK = Weapon('HARPAK', 5, 37.5, 7.5, critC=0.2, critX=2.3,
                 magazine=45, reload=2, firerate=6)

HEMA = Weapon('HEMA', vir=47, critC=0.11, critX=2,
              magazine=60, reload=2, firerate=6)

HIND = (Weapon('HIND_BURST', 7.5, 7.5, 15, critC=0.07, critX=1.5,
               magazine=65, reload=2, firerate=6.25),
        Weapon('HIND_SEMI', 12, 12, 36, critC=0.15, critX=2,
               magazine=65, reload=2, firerate=2.5))

KARAK = Weapon('KARAK', 13, 8.7, 7.3, critC=0.09, critX=1.5,
               magazine=30, reload=2, firerate=11.67)
KARAK_WRAITH = Weapon('KARAK_WRAITH', 14.1, 9.3, 7.8, critC=0.13, critX=2,
                      magazine=60, reload=2, firerate=11.67)

LATRON = Weapon('LATRON', 8.25, 38.5, 8.25, critC=0.12, critX=2,
                magazine=15, reload=2.4, firerate=4.17)
LATRON_PRIME = Weapon('LATRON_PRIME', 9, 72, 9, critC=0.22, critX=2.8,
                      magazine=15, reload=2.4, firerate=4.17)
LATRON_WRAITH = Weapon('LATRON_WRAITH', 15, 42, 3, critC=0.26, critX=2.8,
                       magazine=15, reload=2.4, firerate=5.42)

MUTALIST_QUANTA = Weapon('MUTALIST_QUANTA', 2.5, 15, 7.5, critC=0.025, critX=1.5,
                         magazine=60, reload=3, firerate=10)

OPTICOR = Weapon('OPTICOR', 100, 850, 50, critC=0.2, critX=2.5,
                 magazine=5, reload=2, firerate=1, chargetime=2)

PARACYST = Weapon('PARACYST', txn=33, critC=0.1, critX=2, 
                  magazine=60, reload=2, firerate=11.11)

QUARTAKK = Weapon('QUARTAKK', 18.1, 14.2, 16.7, critC=0.19, critX=2.3,
                  magazine=21, reload=1.9, firerate=6.33, bullets=4)

SOMA = Weapon('SOMA', 1.2, 4.8, 6, critC=0.3, critX=3,
              magazine=100, reload=3, firerate=15)
SOMA_PRIME = Weapon('SOMA_PRIME', 1.2, 4.8, 6, critC=0.3, critX=3,
                    magazine=200, reload=3, firerate=15)

STRADAVAR = (Weapon('STRADAVAR_AUTO', 9.8, 9.8, 8.4, critC=0.25, critX=2,
                    magazine=65, reload=2, firerate=10),
             Weapon('STRADAVAR_SEMI', 7.5, 30, 12.5, critC=0.28, critX=2,
                    magazine=65, reload=2, firerate=5))

SUPRA = Weapon('SUPRA', 4, 30, 6, critC=0.12, critX=1.8,
               magazine=180, reload=3, firerate=12.5)
SUPRA_VANDAL = Weapon('SUPRA_VANDAL', 4, 30, 6, critC=0.16, critX=2,
                      magazine=300, reload=3, firerate=12.5)

SYBARIS = Weapon('SYBARIS', 26.4, 26.4, 27.2, critC=0.25, critX=2,
                 magazine=10, reload=2, firerate=3.98)
DEX_SYBARIS = Weapon('DEX_SYBARIS', 22.5, 18.75, 33.75, critC=0.35, critX=2,
                     magazine=14, reload=1.5, firerate=4.17)
SYBARIS_PRIME = Weapon('SYBARIS_PRIME', 29, 29, 29.9, critC=0.3, critX=2,
                       magazine=20, reload=2, firerate=4.72)

TENORA = (Weapon('TENORA_AUTO', 7.2, 9.6, 7.2, critC=0.28, critX=2,
                 magazine=150, reload=2.5, firerate=11.67),
          Weapon('TENORA_CHARGE', 48, 144, 48, critC=0.34, critX=3,
                 magazine=15, reload=2.5, firerate=10, chargetime=0.8))

TETRA = Weapon('TETRA', imp=6.4, punc=25.6, critC=0.04, critX=1.5,
               magazine=60, reload=2, firerate=6.67)
PRISMA_TETRA = Weapon('PRISMA_TETRA', imp=7.6, punc=30.4, critC=0.1, critX=2,
                      magazine=60, reload=2, firerate=7.08)

TIBERON = Weapon('TIBERON', 11, 22, 11, critC=0.26, critX=2.4,
                 magazine=30, reload=2.3, firerate=9.09)

TIBERON_PRIME = (Weapon('TIBERON_PRIME_BURST', 13.8, 18.4, 13.8, critC=0.28, critX=3,
                        magazine=42, reload=2, firerate=7.38),
                 Weapon('TIBERON_PRIME_SEMI', 13.8, 18.4, 13.8, critC=0.3, critX=3.4,
                        magazine=42, reload=2, firerate=6),
                 Weapon('TIBERON_PRIME_AUTO', 13.8, 18.4, 13.8, critC=0.16, critX=2.8,
                        magazine=42, reload=2, firerate=8.33))

VELDT = Weapon('VELDT', 23.4, 23.4, 43.2, critC=0.22, critX=2.2,
               magazine=16, reload=1.8, firerate=3.67)

ZENITH = (Weapon('ZENITH_AUTO', 4.5, 6, 19.5, critC=0.1, critX=2,
                 magazine=90, reload=1.4, firerate=10.83),
          Weapon('ZENITH_SEMI', 15, 120, 15, critC=0.35, critX=2.5,
                 magazine=18, reload=1.4, firerate=3))

DEX_PIXIA = Weapon('DEX_PIXIA', 16, 16, 128, critC=0.15, critX=2,
                   magazine=60, reload=1, firerate=5.83)

rifle_temp = [BAZA, BOLTOR, BOLTOR_PRIME, TELOS_BOLTOR, \
                BRATON, BRATON_PRIME, BRATON_VANDAL, MK1_BRATON, \
                BURSTON, BURSTON_PRIME, BUZLOK, DERA, \
                DERA_VANDAL, GORGON, PRISMA_GORGON, GORGON_WRAITH, \
                GRAKATA, PRISMA_GRAKATA, GRINLOK, HARPAK, \
                HEMA, KARAK, KARAK_WRAITH, LATRON, \
                LATRON_PRIME, LATRON_WRAITH, MUTALIST_QUANTA, OPTICOR, \
                PARACYST, QUARTAKK, SOMA, SOMA_PRIME, \
                SUPRA, SUPRA_VANDAL, SYBARIS, DEX_SYBARIS, \
                SYBARIS_PRIME, TETRA, PRISMA_TETRA, TIBERON, \
                VELDT, DEX_PIXIA]


rifle_weapons = {x.name: x for x in rifle_temp}

special_rifles = {'ARGONAK': ARGONAK, 'HIND': HIND, 'STRADAVAR': STRADAVAR, 'TENORA': TENORA,
                  'TIBERON_PRIME': TIBERON_PRIME, 'ZENITH': ZENITH}

rifle_weapons.update(special_rifles)

##############################################################



######################### Beam Rifles ########################

AMPREX = Weapon('AMPREX', elec=22, critC=0.32, critX=2.2,
                magazine=200, reload=2.6, firerate=12)

FLUX_RIFLE = Weapon('FLUX_RIFLE', punc=4.8, sla=17.2, critC=0.1, critX=2,
                    magazine=100, reload=2.25, firerate=12)

GLAXION = Weapon('GLAXION', cld=26, critC=0.08, critX=2,
                 magazine=160, reload=2.2, firerate=12)

IGNIS = Weapon('IGNIS', ht=33, critC=0.11, critX=2,
               magazine=150, reload=2, firerate=8)
IGNIS_WRAITH = Weapon('IGNIS_WRAITH', ht=35, critC=0.17, critX=2.5,
                      magazine=200, reload=1.7, firerate=8)

QUANTA = Weapon('QUANTA', elec=20, critC=0.16, critX=2.2,
                magazine=120, reload=2, firerate=12)
QUANTA_CUBE = Weapon('QUANTA_CUBE', blst=600, critC=0.16, critX=2.2,
                     magazine=6, reload=2, firerate=12)
QUANTA_VANDAL = Weapon('QUANTA_VANDAL', elec=26, critC=0.22, critX=2.4,
                       magazine=160, reload=1.8, firerate=12)
QUANTA_VANDAL_CUBE = Weapon('QUANTA_VANDAL_CUBE', blst=600, critC=0.05, critX=2.5,
                            magazine=8, reload=1.8, firerate=4)

SYNAPSE = Weapon('SYNAPSE', crsv=20, critC=0.39, critX=2.7,
                 magazine=140, reload=1.5, firerate=12)


beam_temp = [AMPREX, FLUX_RIFLE, GLAXION, IGNIS, \
             IGNIS_WRAITH, QUANTA, QUANTA_CUBE, QUANTA_VANDAL, \
             QUANTA_VANDAL_CUBE, SYNAPSE]

beam_weapons = {x.name: x for x in beam_temp}

##############################################################



################### Spearguns ################################

FERROX = (Weapon('FERROX', 35, 245, 70, critC=0.32, critX=2.8,
                 magazine=10, reload=2, firerate=1.33, chargetime=0.5),
          Weapon('FERROX_THROWN', 455, 72.5, 122.5, critC=0.04, critX=2,
                 magazine=1, reload=2, firerate=1, chargetime=0.5))

JAVLOK = (Weapon('JAVLOK', ht=230, critC=0.2, critX=2,
                 magazine=6, reload=1.9, firerate=3.33, chargetime=0.3),
          Weapon('JAVLOK_THROWN', 45, 75, 30, critC=0.2, critX=2,
                 magazine=1, reload=0.6, firerate=1, chargetime=0.5))

SCOURGE = (Weapon('SCOURGE', crsv=70, critC=0.02, critX=1.5,
                  magazine=20, reload=2.5, firerate=2.67),
           Weapon('SCOURGE_THROWN', 455, 72.5, 122.5, crsv=50, critC=0.04, critX=2,
                  magazine=1, reload=0.6, firerate=1, chargetime=0.5))


spear_temp = [FERROX, JAVLOK, SCOURGE]

speargun_weapons = {x[0].name: x for x in spear_temp}

##############################################################



################### Shotguns #################################

ARCA_PLASMOR = Weapon('ARCA_PLASMOR', rad=600, critC=0.22, critX=1.6,
                      magazine=10, reload=2.8, firerate=1.1)

ASTILLA = Weapon('ASTILLA', 25.9, 15.4, 28.7, critC=0.17, critX=1.9,
                 magazine=16, reload=2, firerate=4.33)

BOAR = Weapon('BOAR', 12.1, 3.3, 6,6, critC=0.1, critX=1.5,
              magazine=20, reload=2.7, firerate=4.17, bullets=8)
BOAR_PRIME = Weapon('BOAR_PRIME', 26, 6, 8, critC=0.15, critX=2,
                    magazine=20, reload=2.75, firerate=4.67, bullets=8)

CONVECTRIX = Weapon('CONVECTRIX', 1.2, 1.2, 9.6, critC=0.16, critX=2.4,
                    magazine=140, reload=2, firerate=12, bullets=2)

CORINTH = (Weapon('CORINTH', 25.2, 37.8, 27, critC=0.3, critX=2.8,
                  magazine=5, reload=2.3, firerate=1.17, bullets=6),
           Weapon('CORINTH_AIRBURST', blst=404, critC=0.04, critX=1.6,
                  magazine=5, reload=2.3, firerate=1.17))

DRAKGOON = Weapon('DRAKGOON', 7, 7, 56, critC=0.075, critX=2,
                  magazine=7, reload=2.3, firerate=3.33, chargetime=0.5, bullets=10)

HEK = Weapon('HEK', 11.25, 48.75, 15, critC=0.1, critX=2,
             magazine=4, reload=2, firerate=2.17, bullets=7)
VAYKOR_HEK = Weapon('VAYKOR_HEK', 11.25, 48.75, 15, critC=0.25, critX=2,
                    magazine=8, reload=2.25, firerate=3, bullets=7)

KOHM = Weapon('KOHM', 6, 6, 18, critC=0.11, critX=2.3,
              magazine=61.25, reload=2, firerate=3.67, bullets=12)

PHAGE = Weapon('PHAGE', vir=4.29, critC=0.19, critX=2,
               magazine=180, reload=2, firerate=12, bullets=7)

SOBEK = Weapon('SOBEK', 52.5, 8.75, 8.75, critC=0.11, critX=2,
               magazine=20, reload=2.7, firerate=2.5, bullets=5)

STRUN = Weapon('STRUN', 13.75, 3.75, 7.5, critC=0.075, critX=1.5,
               magazine=6, reload=3.75, firerate=2.5, bullets=12)
STRUN_WRAITH = Weapon('STRUN_WRAITH', 26, 6, 8, critC=0.18, critX=2.2,
                      magazine=10, reload=5, firerate=2.5, bullets=10)
MK1_STRUN = Weapon('MK1_STRUN', 9.9, 2.7, 5.4, critC=0.075, critX=2,
                   magazine=6, reload=3.75, firerate=2.08, bullets=10)

TIGRIS = Weapon('TIGRIS', 21, 21, 168, critC=0.1, critX=2,
                magazine=2, reload=1.8, firerate=2, bullets=5)
TIGRIS_PRIME = Weapon('TIGRIS_PRIME', 19.5, 19.5, 156, critC=0.1, critX=2,
                      magazine=2, reload=1.8, firerate=2, bullets=8)
SANCTI_TIGRIS = Weapon('SANCTI_TIGRIS', 21, 21, 168, critC=0.15, critX=1.5,
                       magazine=2, reload=1.5, firerate=2, bullets=6)


shotgun_temp = [ARCA_PLASMOR, ASTILLA, BOAR, BOAR_PRIME, \
                CONVECTRIX, DRAKGOON, HEK, VAYKOR_HEK, \
                KOHM, PHAGE, SOBEK, STRUN, \
                STRUN_WRAITH, MK1_STRUN, TIGRIS, TIGRIS_PRIME, \
                SANCTI_TIGRIS]

shotgun_weapons = {x.name: x for x in shotgun_temp}
shotgun_weapons.update({'CORINTH': CORINTH})

##############################################################



###################### Snipers ###############################

LANKA = Weapon('LANKA', elec=525, critC=0.25, critX=2,
               magazine=10, reload=2, firerate=1, chargetime=1)

RUBICO = Weapon('RUBICO', 144, 27, 9, critC=0.3, critX=3,
                magazine=5, reload=2.4, firerate=2.67)

SNIPETRON = Weapon('SNIPETRON', 18, 144, 18, critC=0.3, critX=1.5,
                   magazine=4, reload=3.5, firerate=2)
SNIPETRON_VANDAL = Weapon('SNIPETRON_VANDAL', 10, 180, 10, critC=0.28, critX=2,
                          magazine=6, reload=2, firerate=2)

VECTIS = Weapon('VECTIS', 90, 78.75, 56.25, critC=0.25, critX=2,
                magazine=1, reload=1, firerate=1.5)
VECTIS_PRIME = Weapon('VECTIS_PRIME', 140, 157.5, 52.5, critC=0.3, critX=2,
                      magazine=2, reload=0.85, firerate=2.67)

VULKAR = Weapon('VULKAR', 180, 33.8, 11.2, critC=0.2, critX=2,
                magazine=6, reload=3, firerate=1.5)
VULKAR_WRAITH = Weapon('VULKAR_WRAITH', imp=245.7, punc=27.3, critC=0.2, critX=2,
                       magazine=8, reload=3, firerate=2)


sniper_temp = [LANKA, RUBICO, SNIPETRON, SNIPETRON_VANDAL, \
               VECTIS, VECTIS_PRIME, VULKAR, VULKAR_WRAITH]

sniper_weapons = {x.name: x for x in sniper_temp}

##############################################################



###################### Bows ##################################

ATTICA = Weapon('ATTICA', 4, 60, 16, critC=0.25, critX=3,
                magazine=20, reload=2.8, firerate=3.67)

CERNOS = Weapon('CERNOS', 198, 11, 11, critC=0.36, critX=2,
                magazine=1, reload=0.6, firerate=0, chargetime=0.5)
CERNOS_PRIME = Weapon('CERNOS_PRIME', 108, 6, 6, critC=0.35, critX=2,
                      magazine=1, reload=0.65, firerate=0, chargetime=0.5, bullets=3)
MUTALIST_CERNOS = (Weapon('MUTALIST_CERNOS', 202.5, 11.25, 11.25, critC=0.15, critX=2,
                          magazine=1, reload=0.6, firerate=0, chargetime=0.5),
                   Weapon('FART CLOUD', txn=50, critC=0.075, critX=1.5,
                          magazine=1, reload=0.6, firerate=1.125))
RAKTA_CERNOS = Weapon('RAKTA_CERNOS', 225, 12.5, 12.5, critC=0.35, critX=2,
                      magazine=1, reload=0.6, firerate=0, chargetime=0.25)

DAIKYU = Weapon('DAIKYU', 138, 184, 138, critC=0.2, critX=2,
                magazine=1, reload=0.6, firerate=0, chargetime=1)

DREAD = Weapon('DREAD', 10, 10, 180, critC=0.5, critX=2,
               magazine=1, reload=0.7, firerate=0, chargetime=0.5)

LENZ = Weapon('LENZ', imp=50, cld=10, blst=660, critC=0.5, critX=2,
              magazine=1, reload=0.6, firerate=1, chargetime=1.2)

PARIS = Weapon('PARIS', 9, 144, 27, critC=0.3, critX=2,
               magazine=1, reload=0.65, firerate=0, chargetime=0.5)
MK1_PARIS = Weapon('MK1_PARIS', 6, 96, 18, critC=0.3, critX=2,
                   magazine=1, reload=0.55, firerate=0, chargetime=0.5)
PARIS_PRIME = Weapon('PARIS_PRIME', 6.5, 208, 45.5, critC=0.45, critX=2,
                     magazine=1, reload=0.7, firerate=0, chargetime=0.5)

ZHUGE = Weapon('ZHUGE', 5, 75, 20, critC=0.2, critX=2,
               magazine=20, reload=2.5, firerate=4.17)

ARTEMIS_BOW = Weapon('ARTEMIS_BOW', 33.6, 192, 14.4, critC=0.25, critX=2,
                     magazine=1, reload=0.6, firerate=0, chargetime=1, bullets=7)


bow_temp = [ATTICA, CERNOS, CERNOS_PRIME, RAKTA_CERNOS, \
            DAIKYU, DREAD, LENZ, PARIS, \
            MK1_PARIS, PARIS_PRIME, ZHUGE, ARTEMIS_BOW]

bow_weapons = {x.name: x for x in bow_temp}
bow_weapons.update({'MUTALIST_CERNOS': MUTALIST_CERNOS})

##############################################################



########################## Launchers #########################

MITER = Weapon('MITER', 12.5, 12.5, 225, critC=0.1, critX=2,
               magazine=20, reload=2, firerate=2.5, chargetime=0.75)

OGRIS = Weapon('OGRIS', blst=700, critC=0.05, critX=2,
               magazine=5, reload=2.5, firerate=1.5, chargetime=0.3)

PANTHERA = (Weapon('PANTHERA', 20, 10, 70, critC=0.12, critX=2,
                   magazine=30, reload=2, firerate=3),
            Weapon('PANTHERA_ALT_FIRE', 10, 10, 80, critC=0.25, critX=2,
                   magazine=60, reload=2, firerate=2))

PENTA = Weapon('PENTA', imp=75, blst=350, critC=0.1, critX=2,
               magazine=5, reload=2.5, firerate=1)
CARMINE_PENTA = Weapon('CARMINE_PENTA', imp=75, blst=350, critC=0.1, critX=2,
                       magazine=10, reload=2.5, firerate=2.7)
SECURA_PENTA = Weapon('SECURA_PETNA', imp=75, blst=300, critC=0.26, critX=2,
                      magazine=7, reload=2.5, firerate=2)

# Note: Not including the Simulor, becuase what even is this shit #

TONKOR = Weapon('TONKOR', punc=75, blst=325, critC=0.25, critX=2.5,
                magazine=2, reload=2, firerate=2)

TORID = (Weapon('TORID', txn=100, critC=0.15, critX=2,
                magazine=5, reload=1.7, firerate=1.5),
         Weapon('TORID_POISON_CLOUD', txn=400, critC=0.15, critX=2,
                magazine=11.25, reload=0, firerate=1.125))

ZARR = (Weapon('ZARR', 24, 40, 16, critC=0.17, critX=2.5,
               magazine=3, reload=2.3, firerate=3, bullets=10),
        Weapon('ZARR_CANNONBALL', imp=25, blst=175, critC=0.17, critX=2.5,
               magazine=3, reload=2.3, firerate=1.67),
        Weapon('ZARR_CLUSTER_BOMBS', blst=50, critC=0.17, critX=2.5,
               magazine=3, reload=2.3, firerate=1.67, bullets=6))


launcher_temp = [MITER, OGRIS, PENTA, CARMINE_PENTA, \
                 SECURA_PENTA, TONKOR]

special_launcher_temp = [PANTHERA, TORID, ZARR]
special_launchers = {x[0].name: x for x in special_launcher_temp}

launcher_weapons = {x.name: x for x in launcher_temp}

launcher_weapons.update(special_launchers)

##############################################################

primary_weapons = {}
primary_weapons.update(rifle_weapons)
primary_weapons.update(beam_weapons)
primary_weapons.update(speargun_weapons)
primary_weapons.update(shotgun_weapons)
primary_weapons.update(sniper_weapons)
primary_weapons.update(bow_weapons)
primary_weapons.update(launcher_weapons)


##############################################################################################################



with open('weapon_data.pickle', 'wb') as f:
    pickle.dump(primary_weapons, f)