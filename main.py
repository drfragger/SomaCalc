from bodytypes import *
from weaponclass import Weapon
from enemyclass import Enemy


Braton = Weapon("Braton", imp=7.9, punc=7.9, sla=8.2,
                critC=0.12, critX=1.6, magazine=60,
                firerate=8.75)


Lancer = Enemy(1, CFlesh, 100, Ferrite, 100)


print(Braton.attack(Lancer))