from bodytypes import *
from weaponclass import Weapon
from enemyclass import Enemy
from graph_function import plot_damage
import modclass as mc
import pickle


with open('enemy_data.pickle', 'rb') as f:
    enem = pickle.load(f)

with open('weapon_data.pickle', 'rb') as f:
    wep = pickle.load(f)



brat_p = wep['BRATON_PRIME']

hevy = enem['O_HEAVY_GUNNER']

plot_damage(brat_p, hevy)

