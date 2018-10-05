from wf_class_defs import Weapon, Enemy
from graph_function import plot_damage
import modclass as mc
import enemy_objects, weapon_objects


WEAPONS = weapon_objects.init()  

ENEMIES = enemy_objects.init()


lancer = ENEMIES['G_LANCER']

baza = WEAPONS['BAZA']

plot_damage(baza, lancer)


