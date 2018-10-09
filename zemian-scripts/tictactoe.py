#!/usr/bin/env python3
# Zemian Deng 2018/10/8
# A simple solution to a tic tac toe game impl.

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

def get_opponent_marker(user_marker):
	if user_marker == 'X':
		return 'O'
	else:
		return 'X'

def ask_whos_first_marker(player_marker):
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
		row = input("Please enter row number to play: ")
		column = input("Please enter column number to play: ")
		row = int(row) - 1
		column = int(column) - 1
		if (row > 2 or row < 0) or \
			(column > 2 or column < 0) or \
			(board[row][column] != ' '):
			print("ERROR: Invalid position, please try again.")
		else:
			done = True
	return (row, column)

def check_two_markers_in_row(row, player_marker):
	if ' ' in row and row.count(player_marker) == 2:
		return row.index(' ')
	else:
		return -1


def about_to_win_pos(board, player_marker):
	'''If a player marker has two markers in a row, column or diagonal, then
	we have a about to win condition.'''
	for i in range(len(board)):
		idx = check_two_markers_in_row(board[i], player_marker)
		if idx >= 0:
			return (0, idx)

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

def get_computer_play_position(board, player_marker):
	# Count number of available spaces in board
	row_indexes = []
	column_indexes = []
	for row in range(len(board)):
		for column in range(len(board[row])):
			if board[row][column] == ' ':
				row_indexes.append(row)
				column_indexes.append(column)

	# Play move position based on how many available space already used up.			
	if len(row_indexes) + len(column_indexes) == 0:
		return random_position(baord, player)
	if len(row_indexes) + len(column_indexes) == 1:
		# If the middle piece is not played, let's take it
		if board[1][1] == ' ':
			return (1, 1)
		else:
			# Well, does not matter which position to play in this case
			return random_position(row_indexes, column_indexes)
	else:
		# Each player already placed atleast one mark, now
		# we need to check for wining moves.

		# Are we going to win?
		win_pos = about_to_win_pos(board, player_marker)
		if win_pos:
			return win_pos
		else:
			# Is opponent has winning move? If yet, block it, else
			# give another random move for now is fine.
			opponent_marker = get_opponent_marker(player_marker)
			win_pos = about_to_win_pos(board, opponent_marker)
			if win_pos:
				return win_pos
			else:
				return random_position(row_indexes, column_indexes)


def random_position(row_indexes, column_indexes):
	# make a copy of lists so we won't change it
	r = list(row_indexes)
	c = list(column_indexes)
	random.shuffle(r)
	random.shuffle(c)
	return (r[0], c[0])


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
			if current_player_marker == user_marker:
				print_board(board)
				row, column = get_user_play_position(board, current_player_marker)
			else:
				row, column = get_computer_play_position(board, current_player_marker)

			board[row][column] = current_player_marker
			if check_wining(board, current_player_marker):
				print_board(board)
				is_computer_player = current_player_marker == computer_marker
				declare_winner(is_computer_player)
				game_over = True
			else:
				current_player_marker = get_opponent_marker(current_player_marker)
				print()

		if not ask_play_again():
			done = True

# Start of the game
main_loop()
