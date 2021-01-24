from turtle import Turtle, Screen
from random import randint, choice

don = Turtle()

don.shape('turtle')
don.color('purple3')
#don.width(10)
don.speed('fastest')
screen = Screen()
screen.colormode(255)


def random_color():
    """
    Returns a random R, G, B color.
    :return: Three integers.
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return r, g, b


def spirograph(circles):
    """
    Takes an integer and creates a spirograph with the inputted amount of circles, each
    with random line colors.
    :param circles: int
    :return: None
    """
    angles = 360 / circles
    for _ in range(circles):
        don.setheading(don.heading() + angles)
        don.pencolor(random_color())
        don.circle(100)


spirograph(120)


# def short_walk():
#     """
#     Creates a short walk with a random color and direction. There are three choices for the direction.
#     (Left, Straight, or Right).
#     :return: None
#     """
#     not_backwards = [-90, 0, 90]
#     current = int(don.heading())
#     don.setheading(current + choice(not_backwards))
#     don.pencolor(random_color())
#     don.forward(15)
#
#
# for _ in range(200):
#     short_walk()


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
