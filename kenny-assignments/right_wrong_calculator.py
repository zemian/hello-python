#
# This program can help you track and count number of problems
# (like chess puzzle exercise) that you have solved, and quickly
# display the correct percentage value for you so you see your
# own progress.
#
# How to use it: This program will display a window with two sides
# for you to click for Wrong or Right count. It then automatically
# calculate your correct percentage and display it.
#
# Author: Zemian Deng
# Date: 09/11/2017
#
# History
# Version: 1.0 - First working program and showed to Kenny!
# Version: 2.0 - Fix "Wrong Count" label and add total count
#

import turtle

# Setup global variables
(width, height) = turtle.screensize()
(width, height) = (width - 100, height - 100)
(start_x, start_y) = (-1 * width, height - 25)
(half_x, half_y) = (0, 25)
wrong_count = 0
right_count = 0

# Define program functions
def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def draw_text(x, y, message):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(message, font=("Arial", 16, "normal"))

def setup_screen_area():
    # Draw initial items on screen when program start. We
    # want two rectangles side by side for capture user click.
    # We want to draw rectangles slightly smaller than the screen size
    # Also note that turtle screensize is only half of the actual windows size!    
    draw_rectangle(start_x, start_y, width, height * 2)
    draw_rectangle(half_x, start_y, width, height * 2)
    draw_rectangle(start_x, start_y, width * 2, 50)

    draw_text(start_x, start_y + 25, "Correct Percentage: 0 %")
    draw_text(half_x + 25, start_y + 25, "Total Count: 0")	
    draw_text(start_x + 25, start_y - 25, "Wrong Count: 0")
    draw_text(half_x + 25, start_y - 25, "Right Count: 0")
    
def clear_rectangle(x, y, width, height):
    # We need to clear the screen canvas for existing text so
    # we can update with new count values.
    turtle.begin_fill()
    orig_color = turtle.color()
    turtle.color("white")
    draw_rectangle(x, y, width, height)
    turtle.end_fill()
    turtle.color(orig_color[0])

def on_click_calc_percentage(x, y):
    # A callback handler to execute when user clicked the screen.
    # We need to reference the "global" variables here.
    global wrong_count, right_count, start_x, start_y, half_x, half_y, width, height, pen
    if (x < 0):
        wrong_count = wrong_count + 1
    else:
        right_count = right_count + 1

    clear_rectangle(start_x - 3, start_y + 50, width * 2, 25)
    clear_rectangle(start_x + 20, start_y - 3, 200, 25)
    clear_rectangle(half_x + 20, start_y - 3, 200, 25)

    total_count = wrong_count + right_count
    percentage = int((right_count / total_count) * 100)
    draw_text(start_x, start_y + 25, "Correct Percentage: {} %".format(percentage))
    draw_text(half_x + 25, start_y + 25, "Total Count: {}".format(total_count))
    draw_text(start_x + 25, start_y - 25, "Wrong Count: {}".format(wrong_count))
    draw_text(half_x + 25, start_y - 25, "Right Count: {}".format(right_count))

# Main program

# Setup graphic for faster screen refresh
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)
turtle.update()

# Register my onclick handler and update screen
turtle.Screen().onclick(on_click_calc_percentage)
setup_screen_area()

# Keep window open until user click X
turtle.mainloop()
