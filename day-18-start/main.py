from turtle import Turtle, Screen
from random import randint

don = Turtle()

don.shape('turtle')
don.color('purple3')
don.width(10)
don.speed(10)
screen = Screen()
screen.colormode(255)


def short_walk():
    don.right(randint(1, 4) * 90)
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    don.pencolor((r, g, b))
    don.forward(20)


for _ in range(100):
    short_walk()


# def draw_shape(sides):
#     """
#     Draws a shape with equal N sides.
#     :param sides: int
#     :return: None
#     """
#     r = randint(1, 255)
#     b = randint(1, 255)
#     g = randint(1, 255)
#
#     for _ in range(sides):
#         don.pencolor((r, g, b))
#         don.forward(100)
#         don.right(360 / sides)


# for i in range(3, 11):
#     draw_shape(i)

screen.screensize(600, 600)
screen.exitonclick()
