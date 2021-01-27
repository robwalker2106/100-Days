from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.amount = -1
        self.score = "Current score: {amount}".format(amount=self.amount)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.gain_point()

    def gain_point(self):
        self.amount += 1
        self.clear()
        self.goto(0, 290)
        self.write("Current score: {amount}".format(amount=self.amount), move=True, align='center')
