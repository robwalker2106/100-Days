from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_OVER = ("Courier", 36, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-300, 260)
        self.score = 0
        self.scored()

    def scored(self):
        self.clear()
        self.goto(-300, 260)
        self.score += 1
        self.write("Level: {s}".format(s=self.score), move=True, align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('black')
        self.write("Game Over", move=True, align='center', font=GAME_OVER)

