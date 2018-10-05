from collections import namedtuple

Body = namedtuple('Body', 'imp punc sla cld elec ht txn blst crsv gas mag rad vir')
Body.__new__.__defaults__ = (1,) * len(Body._fields)

Generic = Body()

CFlesh = Body(imp=0.75, sla=1.25, ht=1.25, gas=0.5, vir=1.75)
Ferrite = Body(punc=1.5, sla=0.85, txn=1.25, blst=0.75, crsv=1.75)
Alloy = Body(punc=1.15, sla=0.5, cld=1.25, elec=0.5, mag=0.5, rad=1.75)
Machinery = Body(imp=1.25, elec=1.5, txn=0.75, blst=1.75, vir=0.75)

Flesh = Body(imp=0.75, sla=1.25, txn=1.5, gas=0.75, vir=1.5)
Shield = Body(imp=1.5, punc=0.8, cld=1.5, txn=0, mag=1.75, rad=0.75)
PShield = Body(imp=1.15, punc=0.5, ht=0.5, txn=0, crsv=0.5, mag=1.75)
Robotic = Body(punc=1.25, sla=0.75, elec=1.5, txn=0.75, rad=1.25)

Infested = Body(sla=1.25, ht=1.25, gas=1.75, rad=0.5, vir=0.5)
IFlesh = Body(sla=1.5, cld=0.5, ht=1.5, gas=1.5)
Fossil = Body(sla=1.15, cld=0.75, txn=0.5, blst=1.5, crsv=1.75, rad=0.75)
Sinew = Body(punc=1.25, cld=1.25, blst=0.5, rad=1.5)



def init():
  return {
    'Generic': Generic,
    'CFlesh': CFlesh,
    'Ferrite': Ferrite,
    'Alloy': Alloy,
    'Machinery': Machinery,
    'Flesh': Flesh,
    'Shield': Shield,
    'PShield': PShield,
    'Robotic': Robotic,
    'Infested': Infested,
    'IFlesh': IFlesh,
    'Fossil': Fossil,
    'Sinew': Sinew
  }


           