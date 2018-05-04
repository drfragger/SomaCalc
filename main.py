from bodytypes import *
from weaponclass import Weapon
from enemyclass import Enemy
from graph_function import plot_damage


Braton = Weapon("Braton", imp=7.9, punc=7.9, sla=8.2,
                critC=0.12, critX=1.6, magazine=45,
                firerate=8.75)

Latron = Weapon("Latron", imp=8.3, punc=38.5, sla=8.2,
                critC=0.12, critX=2, magazine=15,
                firerate=4.17, reload=2.4)


Lancer = Enemy(1, CFlesh, 100, Ferrite, 100)


plot_damage(Braton, Lancer, wep_2 = Latron)
