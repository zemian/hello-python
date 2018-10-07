from turtle import *

# Graph function
def get_y(x):
    return (x * x) / 100

first_x = -400
last_x = 400

# Clear and prepare drawing canvas
delay(.1)
hideturtle()
clear()

# Draw the first dot
penup()
goto(first_x, get_y(first_x))
pendown()
dot()

# Draw the rest of the range of x coordinates
for x in range(first_x + 1, last_x):
    goto(x, get_y(x))
    dot()
    
