import turtle, random
for i in range(100):
    distance = random.randint(1, 100)
    angle = random.randint(0, 360)
    turtle.right(angle)
    turtle.forward(distance)
