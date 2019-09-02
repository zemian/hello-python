import tkinter as tk
import random

# Define GUI constants
WIN_WIDTH = 300
PIECE_WIDTH = WIN_WIDTH / 3

def get_opponent_marker(player_marker):
	'''Given player_marker, return the opposite, or opponent marker.'''
	if player_marker == 'X':
		return 'O'
	else:
		return 'X'

def check_two_markers_in_row(row, player_marker):
	'''Check whether a row of markers contains at least two same player_marker,
	and one empty one. If found, return the index where it is found. If not
	found return -1.'''
	if ' ' in row and row.count(player_marker) == 2:
		return row.index(' ')
	else:
		return -1


def about_to_win_pos(board, player_marker):
	'''Check to see if player_marker on board is about to win or not. If yes, return
	the position that will make the win, else return None.
	The winning position is 3 markers in a row, so if we find two markers with one
	empty space, then that will consider a win pos, and we will return that position.
	'''
	for i in range(len(board)):
		idx = check_two_markers_in_row(board[i], player_marker)
		if idx >= 0:
			return (i, idx)

	idx = check_two_markers_in_row([board[0][0], board[1][0], board[2][0]], player_marker)
	if idx >= 0:
		return (idx, 0)

	idx = check_two_markers_in_row([board[0][1], board[1][1], board[2][1]], player_marker)
	if idx >= 0:
		return (idx, 1)

	idx = check_two_markers_in_row([board[0][2], board[1][2], board[2][2]], player_marker)
	if idx >= 0:
		return (idx, 2)


	idx = check_two_markers_in_row([board[0][0], board[1][1], board[2][2]], player_marker)
	if idx >= 0:
		return (idx, idx)

	idx = check_two_markers_in_row([board[0][2], board[1][1], board[2][0]], player_marker)
	if idx == 0:
		return (0, 2)
	elif idx == 1:
		return (1, 1)
	elif idx == 2:
		return (2, 0)

	return None

def get_available_board_indexes(board):
	'''Return list of tuples. Each tuple is a row and column indexes of empty positionon 
	on the board.'''
	pos = []
	for row in range(len(board)):
		for column in range(len(board[row])):
			if board[row][column] == ' ':
				pos.append((row, column))
	return pos

def get_computer_play_position(board, player_marker):
	'''This is the tic tac toe brain! It still not guarantee to win, but
	will play a decent game. It's missing the strategy for maximum of
	two possible win position check!

	For now, the strategy is if no one play the center, plays it, and
	try to block opponent win, and then if possible, try to win if
	we can.
	'''

	# Collect all the number of available spaces on board as indexes
	available_pos_list = get_available_board_indexes(board)

	# Play move position based on how many available space are available			
	if len(available_pos_list) == 9:
		return random_position(available_pos_list)
	if len(available_pos_list) == 8:
		# If the middle piece is not played, let's take it
		if board[1][1] == ' ':
			return (1, 1)
		else:
			# Well, does not matter which position to play in this case
			return random_position(available_pos_list)
	else:
		# Each player already placed at least one mark, now
		# we need to check for wining moves.

		# Are we going to win?
		win_pos = about_to_win_pos(board, player_marker)
		if win_pos:
			return win_pos
		else:
			# Is opponent has winning move? If yes, block it, else
			# give another random move as next move.
			opponent_marker = get_opponent_marker(player_marker)
			win_pos = about_to_win_pos(board, opponent_marker)
			if win_pos:
				return win_pos
			else:
				return random_position(available_pos_list)

def random_position(available_pos_list):
	'''Shuffle the given indexes and return two random row and column indexes'''
	# We need to make a copy of param lists so we won't change it
	list_copy = list(available_pos_list)
	random.shuffle(list_copy)
	return list_copy[0]


def check_boardfull(board):
	'''Return true if there is no more space on board for markers, else false.'''
	available_pos_list = get_available_board_indexes(board)
	if len(available_pos_list) == 0:
		return True
	else:
		return False

def check_wining(board, player_marker):
	'''If a player marker has 3 markers in a row, column or diagonal, then
	we have a winning condition.'''
	win_str = player_marker * 3
	if ''.join(board[0]) == win_str or \
		''.join(board[1]) == win_str or \
		''.join(board[2]) == win_str or \
		''.join([board[0][0], board[1][0], board[2][0]]) == win_str or \
		''.join([board[0][1], board[1][1], board[2][1]]) == win_str or \
		''.join([board[0][2], board[1][2], board[2][2]]) == win_str or \
		''.join([board[0][0], board[1][1], board[2][2]]) == win_str or \
		''.join([board[0][2], board[1][1], board[2][0]]) == win_str:
		return True
	else:
		return False
	
def declare_winner(is_computer_player):
	if is_computer_player:
		print("****************")
		print("Sorry, you lost!")
		print("****************")
	else:
		print("********")
		print("You won!")
		print("********")

def declare_draw():
	print("********************")
	print("This game is a draw!")
	print("********************")

def play_turn(row, column, game_data):
	''' Return true to continue game, False if game is over'''
	board = game_data['board']
	current_player_marker = game_data['current_player_marker']
	canvas = game_data['canvas']

	draw_piece(canvas, current_player_marker, row, column)

	board[row][column] = current_player_marker
	if check_winning_or_draw(game_data):
		game_over(game_data)
		return False

	return True

def check_winning_or_draw(game_data):
	board = game_data['board']
	current_player_marker = game_data['current_player_marker']
	computer_marker = game_data['computer_marker']
	is_over = False
	# Check for wining and end the game if it's over
	if check_wining(board, current_player_marker):
		is_computer_player = current_player_marker == computer_marker
		declare_winner(is_computer_player)
		is_over = True
	elif check_boardfull(board):
		declare_draw()
		is_over = True
	return is_over

def game_over(game_data):
	tkGUI = game_data['tkGUI']
	tkGUI.quit()
	
# Draw the board
def draw_board(canvas):
	canvas.create_line(PIECE_WIDTH, 0, PIECE_WIDTH, WIN_WIDTH)
	canvas.create_line(PIECE_WIDTH * 2, 0, PIECE_WIDTH * 2, WIN_WIDTH)
	canvas.create_line(0, PIECE_WIDTH, WIN_WIDTH, PIECE_WIDTH)
	canvas.create_line(0, PIECE_WIDTH * 2, WIN_WIDTH, PIECE_WIDTH * 2)

def draw_piece(canvas, marker, row, column):
	x = row * PIECE_WIDTH
	y = column * PIECE_WIDTH
	if marker == 'X':
		canvas.create_line(x, y, x + PIECE_WIDTH, y + PIECE_WIDTH)
		canvas.create_line(x + PIECE_WIDTH, y, x, y + PIECE_WIDTH)
	else:
		inset = 5
		canvas.create_oval(x + inset, 
			y + inset, 
			(x + PIECE_WIDTH) - (inset * 2), 
			(y + PIECE_WIDTH) - (inset * 2))

# Game variables
game_data = {
	'board': [
		  [' ', ' ', ' '], 
		  [' ', ' ', ' '], 
		  [' ', ' ', ' ']],
	'user_marker': 'X',
	'first_marker': 'X',
	'tkGUI': tk.Tk()
}
game_data['computer_marker'] = get_opponent_marker(game_data['user_marker'])
game_data['current_player_marker'] = game_data['first_marker']

# Respond to user click action
def user_click(event):
	global game_data

	# User play:
	board = game_data['board']
	row, column = int(event.x / PIECE_WIDTH), int(event.y / PIECE_WIDTH)
	if board[row][column] != ' ':
		# User should not able to play on position already taken.
		return False
	if play_turn(row, column, game_data):
		# Now computer plays
		current_player_marker = get_opponent_marker(game_data['current_player_marker'])
		game_data['current_player_marker'] = current_player_marker
		row, column = get_computer_play_position(board, current_player_marker)
		play_turn(row, column, game_data)

		# Now switch to user marker again
		current_player_marker = get_opponent_marker(game_data['current_player_marker'])
		game_data['current_player_marker'] = current_player_marker

# Create a canvas for playing area
canvas = tk.Canvas(game_data['tkGUI'], width=WIN_WIDTH, height=WIN_WIDTH)
canvas.bind('<Button-1>', user_click)
draw_board(canvas)
game_data['canvas'] = canvas

# Setup Canvas for display and start listening for GUI events 
canvas.pack()
tk.mainloop()
