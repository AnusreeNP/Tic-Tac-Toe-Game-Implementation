
#import random to call randint() function
import random

#list of 10 strings representing the board
test_board = ['#','X','O','X','O','X','O','X','O','X']

#function for printing the board
def display_board(board):
	print(''+board[7]+'|'+board[8]+'|'+board[9])
	print(''+board[4]+'|'+board[5]+'|'+board[6])
	print(''+board[1]+'|'+board[2]+'|'+board[3])

#function that can take in a player input and assign their marker as 'X' Or 'O'
def player_input():
	letter = ''
	while (letter != 'X' and letter != 'O'):
		print("Do you want to be 'X' or 'O'")
		letter = input()

	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

#function that takes in the board,('X' or 'O'),and a position(number 1-9) and assign it to the board.
def place_marker(board,marker,position):
    board[position] = marker

#function that uses the random module to randomly decide which player goes first.
def choose_first():
	if random.randint(0,1) == 0:
		return player1
	else:
		return player2

#function that asks for player's next position (as a number  1-9)
def player_choice(board):
	pos = ''
	while pos not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(test_board1,int(pos)):
		print("what is your next move(1-9)?")
		pos = input()
	return int(pos)

#function indicating whether a space on the board is freely available.
def space_check(board,pos):
	if board[pos] == " ":
		return True

#function that takes in a board and a mark (X or O)and checks to see if that mark has won
def win_check(board,mark):
	if ((board[7] == mark and board[8] == mark and board[9] == mark) or
	   (board[4] == mark and board[5] == mark and board[6] == mark) or
	   (board[1] == mark and board[2] == mark and board[3] == mark) or
	   (board[7] == mark and board[4] == mark and board[1] == mark) or
	   (board[8] == mark and board[5] == mark and board[2] == mark) or
	   (board[9] == mark and board[6] == mark and board[3] == mark) or
	   (board[7] == mark and board[5] == mark and board[3] == mark) or
	   (board[9] == mark and board[5] == mark and board[1] == mark)):
	  return True

#function that checks if the board is full
def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True

#function that asks thye player if they want to play again
def replay():
	print("Do you want to play again(yes or no)\n")
	if input() == "yes":
		return True
	else:
		return False


print("\n")
display_board(test_board)
print("Welcome to TIC TAC TOE GAME\n")

#Loop if the player needs to play again else break the loop
while True:
	#empty list with 10 spaces
	test_board1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	
	#Assigning X or O to player1 and player2
	player1,player2 = player_input()
	
	#randomly choose the player
	turn = choose_first()
	print('The ' + turn + ' will go first')
	
	#setting the flag for playing the game
	playing_the_game = True
	
	#play the game
	while playing_the_game:
		if turn == player1:
			display_board(test_board1)
			move = player_choice(test_board1)
			place_marker(test_board1,player1,move)
			
			#check for the win case
			if win_check(test_board1,player1):
				display_board(test_board1)
				print("PLAYER1 HAVE WON THE GAME\n")
				playing_the_game = False

			else:
				#check for tie
				if full_board_check(test_board1):
					display_board(test_board1)
					print("THE GAME IS A TIE\n")
					break

				else:
					turn = player2

		else:
			#game for player 2
			display_board(test_board1)
			move = player_choice(test_board1)
			place_marker(test_board1,player2,move)
			
			#check for win case
			if win_check(test_board1,player2):
				display_board(test_board1)
				print("PLAYER2 HAVE WON THE GAME\n")
				playing_the_game = False

			else:
				#check for tie case
				if full_board_check(test_board1):
					display_board(test_board1)
					print("THE GAME IS A TIE\n")
					break

				else:
					turn = player1

	#ask the player to play again
	if replay() == False:
		break








