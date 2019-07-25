# imports multiple clases from the python library and some of our own modules
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine
import os

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ''
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won:
		leaderboard.update(score)
	print ("\nGame Over.")
	name = ''
	n_moves = ''
	leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name
		global moves
		print("\t ===========================================================================================================")
		print("")
		print("\t /////   /////   ////      //  //////  //////     ////   /////  //     //          /|    ////  ")
		print("\t //     //      //        //|  //  //  //        //      //     //     //         / |      /// ")
		print("\t ////    //     //       // |  /////   ////      //      ////   //     //        /  |      //  ")
		print("\t //        ///  //   /  ////|  //      //        //   /  //     //     //       //////    //   ")
		print("\t /////  /////    ////  //   |  //      //////     ////   /////  /////  /////        |   ////// ")
		print("")
		print("\t ===========================================================================================================")
		print("\t * It's midnight and the prison guards are drunk.")
		print("\t * They start a fight tournament between the inmates.")
		print("\t * The winner of the tournament gets a day out of prison.")
		print("\t * There are three other inmates in the tournament left.")
		print("\t * Your mission is to defeat the other three inmates.")
		print("\t * You will have three lives. Good luck!")
		print("")
		print("\t NOTE: To quit, enter :q at any time.")
		name = input("\t Let's play. What is your name? > ")
		difficulty_var = eval(input("\t This game is hard. How many lives do you want? "))
		if (name == ':q'):
			exit(1)
		os.system("clear")
		a_map = Map('round_1')
		a_game = Engine(a_map)
		a_game.lives = difficulty_var
		moves = a_game.play()
		game_over(a_game.won())

play_game()

#leaderboard.print_board()
#test = Score('test',5)
#leaderboard.update(test)
#leaderboard.print_board()
