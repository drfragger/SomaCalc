
# Overview
SomaCalc is a scaling damage calculator for Warframe built in python 3.6.
It has access to both raw numerical output for damage numbers, or you can graph your results to see
how quickly a weapon will fall off at high levels.
Its only external dependancies are [matplotlib](https://matplotlib.org/) and [numpy](http://www.numpy.org/).


# Limitations

- Currently, enemies cannot have shields applied to them. This is because shields have little to no effect on 
enemy survivability, for the most part. The exeptions to this are the Eidolons and the Index opponents at high levels.
As such, I will likely implement a shield system at a later date.

- Does not yet support melee weapons and weapons with unusual fire rates (i.e, Opticor, bows).

- Does not factor in status procs. Not sure if I'll ever manage to get this in reliably, but who knows.

- I haven't set up all of the current weapons and mods yet, so you'll have to add them yourself.

- I am an amateur. There may be bugs, although I haven't encountered anything.