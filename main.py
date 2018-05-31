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



opt = wep['OPTICOR']

modlist = (mc.Serration, mc.HighVoltage)

opt.applymod(modlist)

hevy = enem['O_HEAVY_GUNNER']

print(opt.dmg)

