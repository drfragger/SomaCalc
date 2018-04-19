from Modifiers import *
from ModClass import Mod
import copy

_dmgTypes = ["Imp", "Punc", "Sla", "Cld", "Elec", "Ht", "Txn", "Blst", "Crsv", "Gas", "Mag", "Rad", "Vir"]

Serration = Mod(_dmgTypes, lambda x: x * 2.65, priority=1)

HeavyCaliber = copy.deepcopy(Serration)

VitalSense = Mod(['CritMult'], lambda x: x * 2.2, priority=1)

BladedRounds = copy.deepcopy(VitalSense)


FangedFusillade = Mod(['Sla'], lambda x: x * 2.2, priority=3)

PiercingCalibur = Mod(['Punc'], lambda x: x * 2.2, priority=3)

CrashCourse = Mod(['Imp'], lambda x: x * 2.2, priority=3)

