from player import Player
import world

def get_player_command():
	return raw_input("> ")

def play():
	player = Player()
	print("Escape from Cave Terror!")
	while True:
		
		room = world.tile_at(player.x, player.y)
		print(room.intro_text())
		
		room.modify_player(player)
		action_input = get_player_command()

		if action_input in ['n', 'N']:
			print("Go North!")
			player.move_north()
		elif action_input in ['s', 'S']:
			print("Go South!")
			player.move_south()	
		elif action_input in ['e', 'E']:
			print("Go East!")
			player.move_east()		
		elif action_input in ['w', 'W']:
			print("Go West!")
			player.move_west()
		elif action_input in ['i', 'I']:
			player.print_inventory()	
		elif action_input in ['a', 'A']:
			player.attack()
		else:
			print("Invalid Action!")

play()

