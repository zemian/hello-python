import tkinter as tk

# Define constants
WIN_WIDTH = 300
PIECE_WIDTH = WIN_WIDTH / 3

# Respond to user click action
def setup_user_click(canvas):
	def user_click(event):
		row, column = int(event.x / PIECE_WIDTH), int(event.y / PIECE_WIDTH)
		#print("clicked at row, column:", row, column)
		draw_piece(canvas, 'X', row, column)
	canvas.bind('<Button-1>', user_click)

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


# Create a canvas for playing area
root = tk.Tk()
canvas = tk.Canvas(root, width=WIN_WIDTH, height=WIN_WIDTH)
setup_user_click(canvas)
draw_board(canvas)

# Setup Canvas for display and start listening for GUI events 
canvas.pack()
tk.mainloop()
