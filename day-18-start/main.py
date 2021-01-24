from turtle import Turtle, Screen
from random import randint

don = Turtle()

don.shape('turtle')
don.color('purple3')


sides = 3
screen = Screen()
screen.colormode(255)

for _ in range(3, 10):
    r = randint(1, 255)
    b = randint(1, 255)
    g = randint(1, 255)
    for _ in range(sides):
        don.pencolor((r, g, b))
        don.forward(100)
        don.right(360/sides)
    sides += 1


# for _ in range(4):
#     don.forward(40)
#     don.right(90)
#

# for _ in range(50):
#     don.forward(5)
#     don.penup()
#     don.forward(5)
#     don.pendown()

screen.screensize(600, 600)
screen.exitonclick()
