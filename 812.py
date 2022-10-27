# Daily Coding Problem # 812

# Problem:
# In chess, the Elo rating system is used to calculate player strengths based on game results.
# A simplified description of the Elo system is as follows. Every player begins at the same score.
# For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is.
# For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.
# Implement this system.

class Player:
	def __init__(self, score=1500) -> None:
		self.score = score
	
	def update_score(self, points: int) -> None:
		self.score += points

		# Absolute minimum amount of points to be held
		if self.score < 100:
			self.score = 100

def Elo_outcome(winner: Player, loser: Player, tie=False) -> None:
	def expected_result(player1_score: int, player2_score: int) -> float:
		# Using logistic curve formula with base 10
		# Difference in 200 points is expected win percentage of ~75%
		return 1 / (1 + 10**((player2_score - player1_score) / 400))

	expected_result_winner = expected_result(winner.score, loser.score)

	if tie:
		result_winner = 0.5
	else:
		result_winner = 1
	
	# K-factor constant
	K = 32

	score_difference = round(K * (result_winner - expected_result_winner))

	winner.update_score(score_difference)
	loser.update_score(-score_difference)
	

# ----------------------------------------------------------------------------
# Testing

player1 = Player()
player2 = Player()
Elo_outcome(player1, player2, tie=True)
print(player1.score == player2.score)	# True

player2 = Player(1700)
Elo_outcome(player2, player1)
print(player1.score)					#1492
print(player2.score)					#1708

Elo_outcome(player2, player1, tie=True)
print(player1.score)					#1501
print(player2.score)					#1699

Elo_outcome(player1, player2)
print(player1.score)					#1525
print(player2.score)					#1675