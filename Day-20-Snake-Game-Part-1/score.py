from turtle import Turtle
ALIGN = 'center'
FONT = ('courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.amount = 0
        #self.score = "Current score: {amount}".format(amount=self.amount)
        self.color('white')
        self.hideturtle()
        self.high_score = 0
        self.penup()
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, 277)
        self.write("Score: {amount}  High Score: {high}".format(amount=self.amount, high=self.high_score), move=True,
                   align=ALIGN, font=FONT)

    def gain_point(self):
        self.amount += 1
        self.print_score()

    def reset(self):
        if self.amount >= self.high_score:
            self.high_score = self.amount
            self.print_score()
        self.amount = 0


