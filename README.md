
# Overview
SomaCalc is a scaling damage calculator for Warframe built in Python 3.6.
It has access to both raw numerical output for damage numbers, or you can graph your results to see
how quickly a weapon will fall off at high levels.
Its only external dependancies are [matplotlib](https://matplotlib.org/) and [numpy](http://www.numpy.org/).



# Syntax

### Weapons
All damage type names are abbreviated, for ease of use.
    
    example_weapon = Weapon(name='example_weapon_name',
                            imp=0, punc=0, sla=0,
                            cld=0, elec=0, ht=0, txn=0,
                            blst=0, crsv=0, gas=0, mag=0,
                            rad=0, vir=0,
                            critC=0.1, critX=2,
                            magazine=60, reload_=2, firerate=5, bullets=1,
                            chargetime=0, burstshots=0, burstdelay=0)

### Enemies
All armor, health, etc. types are constants defined in `bodytypes.py`.
They are accessed by calling `bodytypes.init()`.

	import bodytypes
    types = bodytypes.init()
    example_enemy = Enemy(name='example_enemy',
                    baselevel,
                    hptype,
                    basehp,
                    armortype=types['Generic'],
                    basearmor=0,
                    level=30)

With my system, all enemies are techincally armored; unarmored enemies just have a neutral armor type
and zero armor value.

### Mods

    example_mod = Mod( modtype, stat, bonus )
    # modtype can have two different string values: 'damage' or 'other'.
    # 'damage' affects damage stats. 'other' affects anything else.
    # 'stat' can be property the weapon has, or 'all', which indicates a modification to all damage types.
    
    # Note: damage percent bonuses are converted to a multiplier.
    # ex_0: Stormbringer( +90% Electric ) -> Mod('damage', 'elec', 0.9)
    # ex_1: Serration( +160% Damage ) -> Mod('damage', 'All', 1.6)
    
    # Using on a weapon:
    # ex_0 (single mod):
    #       wep = Weapon(etc, etc, ..)
    #       wep.applymod(example_mod)
    
    # ex_1 (multiple mods):
    #       build = (example_mod_0, example_mod_1)          # Must be a tuple, not a list
    #       wep = Weapon(etc, etc, ..)
    #       wep.applymod(build)

### Accessing database of weapons/enemies

    import weapon_objects, enemy_objects

    WEAPONS = weapon_objects.init()
    ENEMIES = enemy_objects.init()
    
    john_prodman = ENEMIES['C_PRODMAN']
    
    grakata = WEAPONS['GRAKATA']

### Graphing DPS

    plot_damage(weapon_0, enemy, weapon_1(optional), level_range=160, live=True)
The `live` parameter determines whether to output a live graph or a static image called `graph-image.png`.
`True` gives the former, and `False` gives the latter.




# Notes

- Enemies with shields are broken up into two "sub enemies"; one with just the shields, 
and the other with the health and armor. As such, damage calculations must be done on each part seperately.

- Does not yet support melee weapons. May need to add new class for that.

- Does not factor in status procs. Not sure if I'll ever manage to get this in reliably, but who knows.

- I'm still not totally satisfied with the mod system yet, as it can't handle changing multiple stats and firerate with burst and charged weapons at the moment.

- ~~All primaries are currently saved in a pickle file. I'm getting around to doing the secondaries.
I'll do the melee weapons once I've figured out how to accurately calculate their DPS.
Also: Pickling works, but I'm unsure if I want to stick with the format.~~ SomaCalc is now pickle-free! Accessing predefined weapons and enemies is now handled by calling the module's instantiator method, which is faster and less cumbersome compared to `pickle`.

- I am an amateur. There may be bugs, although I haven't encountered anything.