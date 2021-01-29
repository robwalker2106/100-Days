from turtle import Turtle


class Ball:

    def __init__(self):
        self.ball = Turtle('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.setheading(35)

    def move_ball(self):
        self.ball.forward(20)

