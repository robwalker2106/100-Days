from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red3')
        self.speed('fastest')
        self.goto(randint(-230, 230), randint(-230, 230))

    def move_food(self):
        new_x = randint(-230, 230)
        new_y = randint(-230, 230)
        self.goto(new_x, new_y)
