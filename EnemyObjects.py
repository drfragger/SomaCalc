from DMGClasses import Weapon, Enemy
from Modifiers import *
import WeaponObjects as W

Lancer = Enemy(1, CFlesh, 100, Ferrite, 100, Level=50)
Lancer.addWeapon(W.Grakata)

CorruptGunner = Enemy(8, CFlesh, 700, Ferrite, 500, Level=100)
CorruptGunner.addWeapon(W.Gorgon)

Nox = Enemy(1, CFlesh, 350, Alloy, 250)
Nox.addWeapon(W.Stug)

Teralyst = Enemy(1, Robotic, 100000, Alloy, 300, ShieldType=Shield, BaseShields=15000, Level=30)


Charger = Enemy(1, Infested, 80)

AncientHealer = Enemy(1, Fossilized, 400)

#Fun fact: Phorid's armor actually increases incoming corrosive damage up until 2475 armor.
Phorid = Enemy(1, Fossilized, 5000, Ferrite, 25)



CorruptBombard = Enemy(4, CFlesh, 300, Alloy, 500, Level=500)

JordasGolem = Enemy(1, Sinew, 20000, Ferrite, 250, Level=34)

Juggernaut = Enemy(15, Infested, 3500, Ferrite, 200)

JuggernautBehemoth = Enemy(1, Infested, 4500, Ferrite, 300, Level=500)

TiaMayn = Enemy(1, Flesh, 150, Alloy, 200, ShieldType=Shield, BaseShields=100, Level=85)

JenDro = Enemy(1, Flesh, 150, Alloy, 200, ShieldType=Shield, BaseShields=100, Level=85)

Excalibur = Enemy(1, Flesh, 100, Ferrite, 225, ShieldType=Shield, BaseShields=100, Level=30)
Excalibur.HP = 300
Excalibur.Shields = 300
Excalibur.Armor = 225

Stalker = Enemy(30, Flesh, 450, Alloy, 300, ShieldType=PShield, BaseShields=200)