from Modifiers import *

class Mod:
	def __init__(self, affectedstats, effect, priority=3):
		self.affectedstats = affectedstats
		self.effect = effect
		self.priority = priority

	def modify(self, Weapon):
		stats = Weapon.__dict__.keys() & self.affectedstats
		for self.affectedstats in stats:
			changedstat = getattr(Weapon, self.affectedstats)
			newStat = self.effect(changedstat)
			setattr(Weapon, self.affectedstats, newStat)

	def __repr__(self):
		return '{}: {} {}'.format(self.__class__.__name__,
								self.affectedstat,
								self.priority)

	def __lt__(self, other):
		return self.priority < other.priority


