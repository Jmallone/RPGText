import items
import world


class Player:
	def __init__(self):
		self.inventory = [items.Rock(),
				items.Dagger(),
				"Gold(5)",
				items.CrustyBread()]
		self.x = 1
		self.y = 2	
		self.hp = 100

	def print_inventory(self):
		print("Inventory: ")
		for item in self.inventory:
			print("* " + str(item))
		best_weapon = self.most_powerful_weapon()
		print("Your best Weapon is your {}".format(best_weapon))

	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:	
				if item.damage > max_damage:
					max_damage = item.damage
					best_weapon = item
			except AttributeError:
				pass
		return best_weapon
	
	def attack(self):
		best_weapon = self.most_powerful_weapon()
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		print("You use {} against {}!".format(best_weapon.name, enemy.name))
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print("You killed {}".format(enemy.name))
		else:
			print("{} HP is {}.".format(enemy.name, enemy.hp))
	
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

	def heal(self):
		consumables = [item for item in self.inventory
				if isinstance(item, item.Consumable)]
		if not consumables:
			print("You don't have any items to heal you!")
			return
