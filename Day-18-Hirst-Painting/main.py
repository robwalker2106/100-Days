#import colorgram as cg
from turtle import Turtle, Screen
from random import choice

#colors = cg.extract('image.jpg', 10)
painting_colors = [(247, 238, 242), (239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147),
                   (165, 59, 48), (140, 184, 162)]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     painting_colors.append((r, g, b))

don = Turtle()
don.hideturtle()
don.speed('fastest')
don.penup()
screen = Screen()
screen.colormode(255)


y = 260.00
x = -260.00


def create_dots(x, y):
    don.setpos(x, y)
    for _ in range(10):
        don.dot(20, choice(painting_colors))
        don.forward(50)


for _ in range(10):
    create_dots(x, y)
    y -= 50



screen.exitonclick()
