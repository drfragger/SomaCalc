from DMGClasses import Weapon, Enemy
from Modifiers import *
import copy

Gorgon = Weapon("Gorgon")
Gorgon.Imp = 18.75
Gorgon.Punc = 3.75
Gorgon.Sla = 2.5
Gorgon.CritMult = 1.5

#Modded
Opticor = Weapon("Opticor")
Opticor.Imp = 415
Opticor.Punc = 3527.5
Opticor.Sla = 207.5
Opticor.Crsv = 7470
Opticor.CritMult = 5.5
Opticor.CritChance = 0.5
Opticor.Reload = 2
Opticor.Bullets = 1.9
Opticor.Magazine = 5
Opticor.FireRate = 0.54288

Braton = Weapon("Braton")
Braton.Imp = 6.6
Braton.Punc = 6.6
Braton.Sla = 6.8
Braton.CritMult = 1.5
Braton.CritChance = 0.1
Braton.FireRate = 8.8
Braton.Bullets = 1
Braton.Magazine = 45
Braton.Reload = 2

Baza = Weapon("Baza")
Baza.Imp = 5.8
Baza.Punc = 6.7
Baza.Sla = 3.5
Baza.CritMult = 2.8

Grakata = Weapon("Grakata")
Grakata.Imp = 6.8
Grakata.Punc = 5.7
Grakata.Sla = 4.5
Grakata.StatusChance = 0.21
Grakata.CritMult = 2.7
Grakata.Magazine = 60
Grakata.Reload = 2.4
Grakata.CritChance = 0.25
Grakata.FireRate = 20
Grakata.Bullets = 1

PrismaGrakata = Weapon("Prisma Grakata")
PrismaGrakata.Imp = 4.4
PrismaGrakata.Punc = 3.7
PrismaGrakata.Sla = 2.9
PrismaGrakata.CritMult = 2.5
PrismaGrakata.StatusChance = 0.2
PrismaGrakata.CritChance = 0.25
PrismaGrakata.Reload = 2
PrismaGrakata.FireRate = 21.67
PrismaGrakata.Magazine = 120
PrismaGrakata.Bullets = 1


Stug = Weapon("Stug")
Stug.Crsv = 156
Stug.CritMult = 1.5

#Modded
VectisPrime = Weapon("Vectis Prime")
VectisPrime.Imp = 559
VectisPrime.Punc = 629.090
VectisPrime.Sla = 209.410
VectisPrime.Rad = 2515.5
VectisPrime.CritMult = 4.4
VectisPrime.FireRate = 2.670
VectisPrime.Reload = 0.9
VectisPrime.Magazine = 2
VectisPrime.Bullets = 2.5
VectisPrime.CritChance = 0.625

#Modded
Rubico = Weapon("Rubico")
Rubico.Imp = 592
Rubico.Punc = 111
Rubico.Sla = 37
Rubico.Crsv = 1332
Rubico.CritMult = 6.6
Rubico.CritChance = 0.625
Rubico.Magazine = 5
Rubico.Reload = 1.935
Rubico.FireRate = 2.670
Rubico.Bullets = 1.9

Corinth = Weapon("Corinth")
Corinth.Imp = 151.2
Corinth.Punc = 226.8
Corinth.Sla = 162
Corinth.CritMult = 2.8
Corinth.Bullets = 6
Corinth.CritChance = 0.3
Corinth.Reload = 2.3
Corinth.Magazine = 5
Corinth.FireRate = 1.17

#Modded
SomaPrime = Weapon("Soma Prime")
SomaPrime.Imp = 4.98
SomaPrime.Punc = 19.92
SomaPrime.Sla = 24.9
SomaPrime.Crsv = 89.64
SomaPrime.CritMult = 6.6
SomaPrime.CritChance = 0.75
SomaPrime.Bullets = 1.9
SomaPrime.FireRate = 28.5
SomaPrime.Magazine = 200
SomaPrime.Reload = 3
SomaPrime.StatusChance = 0.1

#Modded
TigrisPrime = Weapon("Tigris Prime")
TigrisPrime.Imp = 553.8
TigrisPrime.Punc = 553.8
TigrisPrime.Sla = 9746.88
TigrisPrime.Vir = 6645.6
TigrisPrime.Rad = 6645.6
TigrisPrime.CritMult = 2
TigrisPrime.CritChance = 0.1
TigrisPrime.Magazine = 2
TigrisPrime.FireRate = 2
TigrisPrime.Reload = 1.8
TigrisPrime.Bullets = 17.6
TigrisPrime.StatusChance = 1
TigrisPrime.BaseBullets = 8

BoltorPrimeV1 = Weapon("OG Boltor Prime")
BoltorPrimeV1.Imp = 5.5
BoltorPrimeV1.Punc = 49.5
BoltorPrimeV1.CritMult = 2
BoltorPrimeV1.CritChance = 0.05
BoltorPrimeV1.StatusChance = 0.1
BoltorPrimeV1.Bullets = 1
BoltorPrimeV1.Magazine = 60
BoltorPrimeV1.FireRate = 10
BoltorPrimeV1.Reload = 2.4

BoltorPrimeV2 = Weapon("New Boltor Prime")
BoltorPrimeV2.Imp = 4.4
BoltorPrimeV2.Punc = 39.6
BoltorPrimeV2.CritMult = 2
BoltorPrimeV2.CritChance = 0.2
BoltorPrimeV2.StatusChance = 0.24
BoltorPrimeV2.Bullets = 1
BoltorPrimeV2.Magazine = 60
BoltorPrimeV2.FireRate = 10
BoltorPrimeV2.Reload = 2.4

MagnusV1 = Weapon("Old Magnus")
MagnusV1.Imp = 20.3
MagnusV1.Punc = 12.4
MagnusV1.Sla = 12.4
MagnusV1.CritMult = 2
MagnusV1.CritChance = 0.2
MagnusV1.StatusChance = 0.2
MagnusV1.Bullets = 1
MagnusV1.Magazine = 8
MagnusV1.FireRate = 5.83
MagnusV1.Reload = 2

MagnusV2 = copy.deepcopy(MagnusV1)
MagnusV2.Name = "New Magnus"
MagnusV2.Imp = 37.8
MagnusV2.Punc = 23.1
MagnusV2.Sla = 23.1
MagnusV2.StatusChance = 0.25
MagnusV2.CritChance = 0.25
MagnusV2.Reload = 1.6