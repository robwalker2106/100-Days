from turtle import Turtle

ALIGN = 'center'
FONT = ('courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 290)
        self.color('white')
        self.hideturtle()
        self.l_paddle = 0
        self.r_paddle = 0
        self.print_score()

    def print_score(self):
        self.goto(0, 290)
        self.write("Score: {l}         Score: {r}".format(l=self.l_paddle, r=self.r_paddle), move=True,
                   align=ALIGN, font=FONT)

    def player_1_score(self):
        self.l_paddle += 1
        self.clear()
        self.print_score()

    def player_2_score(self):
        self.r_paddle += 1
        self.clear()
        self.print_score()



