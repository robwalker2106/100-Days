from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        self.goto(self.x_move + self.xcor(), self.y_move + self.ycor())

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_paddle()

