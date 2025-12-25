
"""
Staff - Magic Level
Bow - Range Level
Sword - Attack Level
"""

class Weapon:
	def __init__(self, weapon_class):
		self.weapon_class = weapon_class

	def stats(self):
		print(f"{self.weapon_class} Has no stats")



magic = Weapon("Staff")
range = Weapon("Bow")
melee = Weapon("Scimitar")

magic.stats()


def bestSeat(seats):
	pass