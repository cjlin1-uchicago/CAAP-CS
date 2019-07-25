# imports random module form library
#imports time module from library
#imports os module from library
import random
import time
import os

# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

#Scene 1
class FatalFistFred(Scene):

	name = "Fatal Fist Freddie"

	#Defining life points and move count
	def __init__(self):
		self.r1_moves = 0
		self.self_life = 20
		self.fred_life = 20

	def enter(self):
		print("\t ======================================================")
		print("\t ROUND 1: FATAL FIST FREDDIE")
		print("\t ======================================================")
		print("\t - In this round, no weapons are allowed.")
		print("\t - You and Fred will begin with 20 life points.")
		print("\t - The first to lose all 20 points will be the loser.")
		print("\t - Each move will vary in damage and speed bonus.")
		print("\t - Damage points are modified randomly by the speed bonus.")
		print("\t ======================================================")
		return self.action()

	def action(self):
		#Menu of moves
		def menu_1():
			print("")
			print("\t       Attack        Damage        Speed Bonus")
			print("\t --------------------------------------------------")
			print("\t [1]   Punch         3             3")
			print("\t [2]   Slap          2             4")
			print("\t [3]   Kick          4             2")
			print("\t [4]   Dodge         0             0")
			print("")
			print("\t You:", round(self.self_life,2))
			print("\t Fred:", round(self.fred_life,2))
			print("")
			print("\t What will you do?")

		#Makes Fred's decisions
		def fred_attacks():
			move_names = ["PUNCH","SLAP","KICK","DODGE"]
			move_damage = [3*(1+random.uniform(0,3)/10), 2*(1+random.uniform(0,4)/10), 4*(1+random.uniform(0,2)/10), 0]
			m = random.randint(0,3)
			print("\t                     Fred used", move_names[m]+"!")
			print("\t +++++++++++++++++++++++++++++++++++++++++++++")
			if m == 3:
				self.fred_life = self.fred_life
			else:
				self.fred_life = self.fred_life - d
				self.self_life = self.self_life - move_damage[m]

		#Loop for battling
		while self.self_life >0 and self.fred_life >0:
			print("\t                     MOVE:", self.r1_moves)
			print("")
			menu_1()
			user = eval(input("\t Your Move:"))
			os.system("clear")
			if (user == ':q'):
				exit(1)
			elif user == 1:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used PUNCH!")
				d = 3*(1+random.uniform(0,3)/10)
				fred_attacks()
				self.r1_moves = self.r1_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Fred:", round(self.fred_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			elif user == 2:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used SLAP!")
				d = 2*(1+random.uniform(0,4)/10)
				fred_attacks()
				self.r1_moves = self.r1_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Fred:", round(self.fred_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			elif user == 3:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used KICK!")
				d = 4*(1+random.uniform(0,2)/10)
				fred_attacks()
				self.r1_moves = self.r1_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Fred:", round(self.fred_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			elif user == 4:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used DODGE!")
				d = 0
				self.self_life = self.self_life
				self.fred_life = self.fred_life
				self.r1_moves = self.r1_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Fred:", round(self.fred_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			if self.self_life <= 0 or self.fred_life <= 0:
				break

		#Win/lose directing
		if self.self_life >= self.fred_life:
			print("\t We have a winner!")
			return self.exit_scene('round_2')
		else:
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		#Resets life points
		self.self_life = 20
		self.fred_life = 20
		return outcome

class SwordSwingingSteve(Scene):

	name = "Sword Swinging Steve"

	#Defining life points and move count
	def __init__(self):
		self.r2_moves = 0
		self.self_life = 40
		self.steve_life = 40

	def enter(self):
		print("\t ======================================================")
		print("\t ROUND 2: SWORD SWINGING STEVE")
		print("\t ======================================================")
		print("\t - This round, you and Steve will use two really heavy swords.")
		print("\t - The first to lose all 40 points will be the loser.")
		print("\t - Steve can deal full damage per move.")
		print("\t - However, the sword is too heavy for you.")
		print("\t - Each strike has a different probability of success")
		print("\t ======================================================")
		return self.action()

	def action(self):
		#Menu of moves
		def menu_2():
			print("")
			print("\t       Attack        Damage      Percent Chance of Dealing Damage")
			print("\t -------------------------------------------------------------------")
			print("\t [1]   Swing         5           80")
			print("\t [2]   Stab          10          25")
			print("\t [3]   Stun          8           60")
			print("\t [4]   Dodge         0           100")
			print("")
			print("\t You:", round(self.self_life,2))
			print("\t Steve:", round(self.steve_life,2))
			print("")
			print("\t What will you do?")

		#Makes Steve's decisions
		def steve_attacks():
			move_names = ["SWING","STAB","STUN","DODGE"]
			move_damage = [5,10,8,0]
			m = random.randint(0,3)
			print("\t                     Steve used", move_names[m]+"!")
			print("\t +++++++++++++++++++++++++++++++++++++++++++++")
			if m == 3:
				self.steve_life = self.steve_life
			else:
				self.steve_life = self.steve_life - d
				self.self_life = self.self_life - move_damage[m]

		#Loop for battling
		while self.self_life >0 and self.steve_life >0:
			print("\t                     MOVE:", self.r2_moves)
			print("")
			menu_2()
			user = eval(input("\t Your Move:"))
			os.system("clear")
			if (user == ':q'):
				exit(1)
			elif user == 1:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used SWING!")
				if random.uniform(0,1) <= 0.8:
					d = 5
				else:
					d = 0
					print(" ")
					print("\t You missed!")
					print(" ")
				steve_attacks()
				self.r2_moves = self.r2_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Steve:", round(self.steve_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			elif user == 2:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used STAB!")
				if random.uniform(0,1) <= 0.25:
					d = 10
				else:
					d = 0
					print(" ")
					print("\t You missed!")
					print(" ")
				steve_attacks()
				self.r2_moves = self.r2_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Steve:", round(self.steve_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			elif user == 3:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used STUN!")
				if random.uniform(0,1) <= 0.6:
					d = 8
				else:
					d = 0
					print(" ")
					print("\t You missed!")
					print(" ")
				steve_attacks()
				self.r2_moves = self.r2_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Steve:", round(self.steve_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			elif user == 4:
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used DODGE!")
				d = 0
				self.self_life = self.self_life
				self.steve_life = self.steve_life
				self.r2_moves = self.r2_moves + 1
				print("\t You:", round(self.self_life,2))
				print("\t Steve:", round(self.steve_life,2))
				print("")
				time.sleep(3)
				os.system('clear')
			if self.self_life <= 0 or self.steve_life <= 0:
				break

		#Win/lose directing
		if self.self_life >= self.steve_life:
			print("\t We have a winner!")
			return self.exit_scene('round_3')
		else:
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		#Resets life points
		self.self_life = 40
		self.steve_life = 40
		return outcome

class PennyPuncherPerry(Scene):

	name ='Penny Puncher Perry'

	#Defining life points and move count
	def __init__(self):
		self.r3_moves = 0
		self.self_life = 15
		self.perry_life = 15

	def enter(self):
		print("\t ======================================================")
		print("\t ROUND 3: Penny-Puncher Perry")
		print("\t ======================================================")
		print("\t - This round, you and Perry will play rock paper scissors until someone is knocked out.")
		print("\t - The winner of each throw will deal a punch of 3 damage points.")
		print("\t - You and Perry will have 15 life points.")
		print("\t - The first to lose all 15 points will be the loser.")
		print("\t ======================================================")
		return self.action()

	def action(self):
		#Menu of moves
		def menu_3():
			print("\t       Throw Options")
			print("\t ------------------------------------------------------")
			print("\t [1]   Rock")
			print("\t [2]   Paper")
			print("\t [3]   Scissors")
			print("")
			print("\t You:", round(self.self_life,2))
			print("\t Perry:", round(self.perry_life,2))
			print("")
			print("\t What will you do?")

		move_names = ["ROCK","PAPER","SCISSORS"]

		#Loop for battling
		while self.self_life >0 and self.perry_life >0:
			print("\t                     Move:", self.r3_moves)
			print("")
			menu_3()
			user = eval(input("\t Your Move:"))
			os.system("clear")
			if (user == ':q'):
				exit(1)
			elif user == 1:
				self.r3_moves = self.r3_moves + 1
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used ROCK!")
				perry_attack = move_names[random.randint(0,2)]
				print("\t                     Perry used "+perry_attack+"!")
				if perry_attack == "ROCK":
					print("\t Draw!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				if perry_attack == "PAPER":
					print("\t You took a hit!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					self.self_life = self.self_life - 3
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				if perry_attack == "SCISSORS":
					print("\t Perry takes a hit!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					self.perry_life = self.perry_life - 3
					print("\t You: ", self.self_life)
					print("\t Perry: ", self.perry_life)
				time.sleep(3)
				os.system('clear')
			if user == 2:
				self.r3_moves = self.r3_moves + 1
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used PAPER!")
				perry_attack = move_names[random.randint(0,2)]
				print("\t                     Perry used "+perry_attack+"!")
				if perry_attack == "PAPER":
					print("\t Draw!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				if perry_attack == "SCISSORS":
					print("\t You took a hit!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					self.self_life = self.self_life - 3
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				if perry_attack == "ROCK":
					print("\t Perry takes a hit!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					self.perry_life = self.perry_life - 3
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				time.sleep(3)
				os.system('clear')
			if user == 3:
				self.r3_moves = self.r3_moves + 1
				print("\t +++++++++++++++++++++++++++++++++++++++++++++")
				print("\t You used SCISSORS!")
				perry_attack = move_names[random.randint(0,2)]
				print("\t                     Perry used "+perry_attack+"!")
				if perry_attack == "SCISSORS":
					print("\t Draw!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				if perry_attack == "ROCK":
					print("\t You took a hit!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					self.self_life = self.self_life - 3
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				if perry_attack == "PAPER":
					print("\t Perry takes a hit!")
					print("\t +++++++++++++++++++++++++++++++++++++++++++++")
					self.perry_life = self.perry_life - 3
					print("\t You:", self.self_life)
					print("\t Perry:", self.perry_life)
				time.sleep(3)
				os.system('clear')
				if self.self_life <= 0 or self.perry_life <= 0:
					break
		#Win/lose directing
		if self.self_life >= self.perry_life:
			print("\t We have a winner!")
			return self.exit_scene('round_4')
		else:
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		#Resets life points
		self.self_life = 15
		self.perry_life = 15
		return outcome

class MathIsHard(Scene):

	name = 'Math is Hard'

	def enter(self):
		("\t ======================================================")
		print("\t ROUND 4: Math is Hard")
		print("\t ======================================================")
		print("\t So you've made it to the last round.")
		print("\t But wait, the guards aren't going to let you leave yet.")
		print("\t They have one last challenge up their sleeve:")
		print("\t +++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t Compute 1+5!")
		print("\t +++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t [1] 6")
		print("\t [2] 21")
		print("\t [3] 121")
		return self.action()

	def action(self):
		#Requests answer to question
		user = eval(input("\t What is your answer? "))
		if (user == ':q'):
			exit(1)
		elif user == 1:
			print("\t WRONG!")
			return self.exit_scene('death')
		elif user == 2:
			print("\t WRONG")
			return self.exit_scene('death')
		elif user == 3:
			print("\t CORRECT!!!")
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		time.sleep(5)
		os.system('clear')
		return outcome
