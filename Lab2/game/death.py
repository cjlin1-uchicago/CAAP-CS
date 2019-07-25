#importing random int maker module
#imports time module from library
from random import randint
import time

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["Oof! You just got pounded!",
			"Nice try, pal.",
			"Guess you're not getting out soon..."
			]
	def enter(self):
		print("\t XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("\t", Death.quips[randint(0, len(self.quips)- 1)])
		print("\t XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		time.sleep(3)
		return 'died'
