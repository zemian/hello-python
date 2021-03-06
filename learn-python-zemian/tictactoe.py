#!/usr/bin/env python3
# Zemian Deng 2018/10/8
#
# A simple solution to a tic tac toe game written in python3
#

import random

def welcome():
	print("Welcome to Tic Tac Toe game.")
	print("-- You can press CTRL+C to quit any time.")
	print()

def ask_user_marker():
	done = False
	while not done:
		answer = input("Which marker do you want to use? Enter X or O: ")
		answer = answer.upper()
		if answer == 'X' or answer == 'O':
			done = True
		else:
			print("ERROR: Invalid input, please try again.")
	return answer

def get_opponent_marker(player_marker):
	'''Given player_marker, return the opposite, or opponent marker.'''
	if player_marker == 'X':
		return 'O'
	else:
		return 'X'

def ask_whos_first_marker(player_marker):
	'''Ask if user want to play first or not. If yes, we will return player_marker,
	else will return the opponent marker.'''
	done = False
	while not done:
		answer = input("Do you want to go first? Enter YES or NO: ")
		answer = answer.upper()
		if answer == 'YES' or answer == 'NO':
			done = True
		else:
			print("ERROR: Invalid input, please try again.")

	if answer == 'YES':
		return player_marker
	else:
		return get_opponent_marker(player_marker)

def print_board(board):
	print('|'.join(board[0]))
	print('-----')
	print('|'.join(board[1]))
	print('-----')
	print('|'.join(board[2]))

def get_user_play_position(board, player_marker):
	'''Ge user input on position to play. User need to enter row and column numbers,
	and we will return zero based index of row and column.'''
	done = False
	while not done:
		print("You are playing {}".format(player_marker))
		answer = input("Please enter row,column number to play: ")
		row, column = answer.split(',')
		try:
			row = int(row) - 1
			column = int(column) - 1
			if (row > 2 or row < 0) or \
				(column > 2 or column < 0) or \
				(board[row][column] != ' '):
				print("ERROR: Invalid position, please try again.")
			else:
				done = True
		except:
			print("ERROR: Invalid position, please try again.")

	return (row, column)

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

def ask_play_again():
	done = False
	while not done:
		answer = input("Do you want to play again? Enter YES or NO: ")
		answer = answer.upper()
		if answer == 'YES' or answer == 'NO':
			done = True
		else:
			print("ERROR: Invalid input. Please try again.")
			
	if answer == 'YES':
		return True
	else:
		return False

def main_loop():
	welcome()

	done = False
	while not done:
		board = [
		  [' ', ' ', ' '], 
		  [' ', ' ', ' '], 
		  [' ', ' ', ' ']
		]
		user_marker = ask_user_marker()
		computer_marker = get_opponent_marker(user_marker)
		first_marker = ask_whos_first_marker(user_marker)
		current_player_marker = first_marker
		game_over = False

		while not game_over:
			# Get marker from player. We will print board if it's user turn only.
			if current_player_marker == user_marker:
				print_board(board)
				row, column = get_user_play_position(board, current_player_marker)
			else:
				row, column = get_computer_play_position(board, current_player_marker)

			# Set the marker on board!
			if board[row][column] != ' ':
				# This should not happen, but added for safety check to ensure game
				# is not corrupted
				print("ERROR: Player selected invalid position: {} {}".format(row, column))
				available_pos_list = get_available_board_indexes(board)
				print("DEBUG: available_pos_list={}".format(available_pos_list))
			else:	
				board[row][column] = current_player_marker

			# Check for wining and end the game if it's over
			if check_wining(board, current_player_marker):
				print_board(board)
				is_computer_player = current_player_marker == computer_marker
				declare_winner(is_computer_player)
				game_over = True
			elif check_boardfull(board):
				print_board(board)
				declare_draw()
				game_over = True
			else:
				current_player_marker = get_opponent_marker(current_player_marker)
				print()

		if not ask_play_again():
			done = True
		else:
			print("Good Bye!")

# Start of the game
main_loop()
