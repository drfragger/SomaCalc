from Modifiers import *



def EnemyArmorScale(BaseArmor, CurrentLevel, BaseLevel):
    '''
    Returns the armor value for the enemy at the specified level.
    '''
    etc = 1 + (((CurrentLevel - BaseLevel)**1.75) * 0.005)
    result = BaseArmor * etc
    return result

#Returns a DMGMod value for use in the ArmorDMG method
def ArmorMod(DMGType, HealthType, ArmorType, Armor, CritMult=1, BodyMult=1):
    '''
    Redux due to armor is the reciprocal of 1 + (Armor / 300), after Armor val is changed
    due to elemental factors.
    The redux is then multiplied by the product of all damage multipliers.
    '''

    HPMod = getattr(HealthType, DMGType)
    ARMod = getattr(ArmorType, DMGType)
    DMGPart = HPMod * ARMod * CritMult * BodyMult
    ArmorPart = Armor * (2 - ARMod)
    ArmorFactor = (ArmorPart / 300) + 1
    result = DMGPart / ArmorFactor
    return result

def ArmorDMG(BaseDMG, DMGMod):
    '''
    Note: DMGMod comes from ArmorMod.
    '''
    result = BaseDMG * DMGMod
    return result

def HealthScale(BaseHP, CurrentLevel, BaseLevel):
    modif = 1 + ((CurrentLevel - BaseLevel)**2 * 0.015)
    HP = BaseHP * modif
    return HP

def EffectiveHealth(HP, Armor):
    '''
    EffectiveHealth(HP, Armor)
    Calculates EHP based on current Health and Armor.
    [Enemy] class has an EHP() method anyway, so this is
    mostly for testing.
    '''
    DMGRedux = (1 - 300/(300 + Armor))
    rdx = 1 - DMGRedux
    EHP = HP / rdx
    return EHP
