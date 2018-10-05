import bodytypes


types = bodytypes.init()


def armor_scaling(entity):
    b_armor = entity.baseprops['basearmor']
    b_level = entity.baseprops['baselevel']
    c_level = entity.level
    
    return b_armor * (1 + (c_level - b_level)**1.75 * 0.005)




def health_scaling(entity):
    b_hp = entity.baseprops['basehp']
    b_level = entity.baseprops['baselevel']
    c_level = entity.level
    
    scale_type = entity.basetypes['hptype']
    scale_modifier = 0.015         # Default for HP.
    
    if (scale_type is types['Shield']) or (scale_type is types['PShield']):
        scale_modifier = 0.0075    # Default for Shields.
    
    return b_hp * (1 + (c_level - b_level)**2 * scale_modifier)


def damage(wep_damage, element, entity, crit_mult=1):
    
    hp_modifier = getattr(entity.basetypes['hptype'], element)
    armor_modifier = getattr(entity.basetypes['armortype'], element)
    
    net_modifier = hp_modifier * armor_modifier * crit_mult
    
    armor_redux = 1 + ((entity.props['armor'] * (2 - armor_modifier)) / 300)
    
    overall_redux = net_modifier / armor_redux
    
    return wep_damage * overall_redux



def damage_mitigation(element, entity):
    
    hp_modifier = getattr(entity.basetypes['hptype'], element)
    armor_modifier = getattr(entity.basetypes['armortype'], element)
    
    net_modifier = hp_modifier * armor_modifier
    armor_redux = 1 + ((entity.props['armor'] * (2 - armor_modifier)) / 300)
    overall_redux = net_modifier / armor_redux
    
    return overall_redux
    