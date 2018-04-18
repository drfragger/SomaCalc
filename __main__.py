from Modifiers import *
from Damage import *
from DMGClasses import Weapon, Enemy
import matplotlib.pyplot as plt
import numpy as np






def plotDamage(Tool:Weapon, Victim:Enemy, Tool2:Weapon=None, LevelRange=100):
	domain = np.arange(Victim.BaseLevel, LevelRange, 0.01)
	DMGSponge = Enemy(Victim.BaseLevel, Victim.HPType, Victim.BaseHP, Victim.ArmorType, Victim.BaseArmor, \
		Level=domain);

	#Burst Plot
	plt.subplot(2, 1, 1)

	tool1critdesc = '{0} (Crit)'.format(Tool.Name)

	plt.plot(domain, Tool.returnBurst(DMGSponge), label=Tool.Name)

	plt.plot(domain, Tool.returnBurst(DMGSponge, isCrit=True), label=tool1critdesc)
	
	if Tool2 is not None:
		tool2critdesc = '{0} (Crit)'.format(Tool2.Name)
		plt.plot(domain, Tool2.returnBurst(DMGSponge), '--', label=Tool2.Name)
		plt.plot(domain, Tool2.returnBurst(DMGSponge, isCrit=True), '--', label=tool2critdesc)


	plt.ylabel("Burst")
	plt.title("DPS Charts")
	plt.legend()
	plt.grid(True)

	#Sustained Plot
	plt.subplot(2, 1, 2)

	plt.plot(domain, Tool.returnSustained(DMGSponge), label=Tool.Name)
	plt.plot(domain, Tool.returnSustained(DMGSponge, isCrit=True), label=tool1critdesc)
	
	if Tool2 is not None:
		plt.plot(domain, Tool2.returnSustained(DMGSponge), '--', label=Tool2.Name)
		plt.plot(domain, Tool2.returnSustained(DMGSponge, isCrit=True), '--', label=tool2critdesc)

	plt.ylabel("Sustained")
	plt.xlabel("Enemy Level")
	plt.legend()
	plt.grid(True)
	plt.show()





print("THIS IS THE TEST BRANCH PLEASE IGNORE")

