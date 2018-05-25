from bodytypes import *
from weaponclass import Weapon
from enemyclass import Enemy
import numpy as np
import matplotlib.pyplot as plt


def plot_damage(wep_1:Weapon, victim, wep_2:Weapon=None, level_range=100):
    
    domain = np.arange(victim.baseprops['baselevel'], level_range, 0.01)
    
    dmg_sponge = Enemy(victim.name, victim.baseprops['baselevel'],
                       victim.basetypes['hptype'],
                       victim.baseprops['basehp'],
                       victim.basetypes['armortype'],
                       victim.baseprops['basearmor'],
                       level=domain)
    
    #Burst Plot
    
    plt.subplot(2, 1, 1)
    
    wep_1critdesc = f'{wep_1.name} (Crit)'
    
    plt.plot(domain, wep_1.get_burst(dmg_sponge), label=wep_1.name)
    
    plt.plot(domain, wep_1.get_burst(dmg_sponge, isCrit=True), label=wep_1critdesc)
    
    if wep_2 is not None:
        wep_2critdesc = '{0} (Crit)'.format(wep_2.name)
        plt.plot(domain, wep_2.get_burst(dmg_sponge), '--', label=wep_2.name)
        plt.plot(domain, wep_2.get_burst(dmg_sponge, isCrit=True), '--', label=wep_2critdesc)


    plt.ylabel("Burst")
    plt.title("DPS Graph for {}".format(victim.name))
    plt.legend()
    plt.grid(True)

    #Sustained Plot
    plt.subplot(2, 1, 2)

    plt.plot(domain, wep_1.get_sustained(dmg_sponge), label=wep_1.name)
    plt.plot(domain, wep_1.get_sustained(dmg_sponge, isCrit=True), label=wep_1critdesc)

    if wep_2 is not None:
        plt.plot(domain, wep_2.get_sustained(dmg_sponge), '--', label=wep_2.name)
        plt.plot(domain, wep_2.get_sustained(dmg_sponge, isCrit=True), '--', label=wep_2critdesc)

    plt.ylabel("Sustained")
    plt.xlabel("Enemy Level")
    plt.legend()
    plt.grid(True)
    plt.show()    