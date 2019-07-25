# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		for i in range(self.size):
			name = "Player"+str(i)
			moves = 1000
			score = Score(name,moves)
			self.board.append(score)

	# prints the leaderboard
	def print_board(self):
		print("\t ========== LEADERBOARD ==========")
		for rank in range(self.size):
			play_name = self.board[rank].get_name()
			play_score = self.board[rank].get_score()
			print("\t",play_name + "\t \t" + str(play_score))


	# checks if given score should be in the leaderboard
	def update(self, score):
		for i in range(self.size):
			if score.get_score() < self.board[i].get_score():
				self.insert(score,i)
				break


	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, i):
		#edit_from = i
		for r in range(self.size-1, i):
			self.board[r] , self.board[r-1] = self.board[r-1], self.board[r]
		self.board[i] = score
