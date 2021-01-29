from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.setheading(65)

    def move_ball(self):
        self.forward(10)

    def change_direction(self):
        if 90 > self.heading() > 0:
            self.setheading(self.heading() - 90)

