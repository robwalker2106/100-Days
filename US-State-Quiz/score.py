from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('black')
        self.hideturtle()
        self.score = 0
        self.score_print()

    def score_print(self):
        self.goto(0, 300)
        self.clear()
        self.write('States Found {}/50'.format(self.score), move=True, align='center', font=FONT)

    def add_point(self):
        self.score += 1
        self.score_print()
