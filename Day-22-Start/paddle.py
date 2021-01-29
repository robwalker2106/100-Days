from turtle import Turtle


class Paddle:
    def __init__(self, starting_position):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.goto(starting_position)

    def move_wall_up(self):
        self.paddle.setheading(90)
        self.paddle.forward(20)

    def move_wall_down(self):
        self.paddle.setheading(270)
        self.paddle.forward(20)
