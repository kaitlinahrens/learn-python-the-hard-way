from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		curent_scene = self.scene_map.opening_scene()

		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [
			"You died. You aren't very good at this.",
			"Damn. You suck.",
			"See ya in the next life."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCooridor(Scene):

	def enter(self):
		print "Huge pirate ships have stationed themselves around your house boat"
		print "and killed your family. You are the last surviving human for miles"
		print "around. Little do the pirates know, you are part of a massive task"
		print "force that specializes in the annihilation of pirates. Your commander"
		print "has given you one last mission: active the self-destruct funtion on"
		print "the master ship."
		print "\n"
		print "You've jumped your ship and made it into the ship in between yours"
		print "and the master. You're running down the side of the ship when a pirate"
		print "jumps out from behind a barrel and pulls a sword on you."

		action = raw_input("> ")

		if action == "shoot!":
			print "You miss the pirate entirely because your nerves are so shot."
			print "He bashes you upside the head with his sword, takes your gun,"
			print "and shoots you in the face."
			return 'death'

		elif action == "grab sword":
			print "He loses his grip because he's had a bit too much rum. You"
			print "take the sword, pierce his heart, steal his sheath and run."
			return 'master_ship'

		else:
			print "DOES NOT COMPUTE!"
			return 'central_cooridor'

class MasterShip(Scene):

	def enter(self):
		print "You have made it to the master ship. You find the control room"
		print "abandoned because these pirates are idiots. You find the switch"
		print "and the ship blows up instantly."
		return 'death'







































