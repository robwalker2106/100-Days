from turtle import Turtle
ALIGN = 'center'
FONT = ('courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.amount = 0
        self.score = "Current score: {amount}".format(amount=self.amount)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 277)
        self.print_score()

    def print_score(self):
        self.goto(0, 277)
        self.write("Current score: {amount}".format(amount=self.amount), move=True, align=ALIGN, font=FONT)

    def gain_point(self):
        self.amount += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=True, align=ALIGN, font=FONT)

