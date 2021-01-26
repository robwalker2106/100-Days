from turtle import Turtle, Screen
from random import randint

color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

y = 0
c = 0

for i in color:
    i = Turtle(shape='turtle')
    i.color(color[c])
    i.penup()
    i.goto(-230, y)
    y += 30
    c += 1
    turtles.append(i)

screen = Screen()
screen.setup(width=500, height=400)

turtle_line = Turtle()
turtle_line.hideturtle()
turtle_line.penup()
turtle_line.goto(209, 160)
turtle_line.pendown()
turtle_line.setheading(-90)
turtle_line.forward(170)
turtle_line.penup()
turtle_line.goto(-210, 160)
turtle_line.pendown()
turtle_line.forward(170)

turtle_bet = screen.textinput("Make your bet", "Which turtle will when the race? Choose color: ")
winner = ''

race_over = False
while not race_over:
    for turtle in turtles:
        turtle.forward(randint(5, 16))
        if turtle.position()[0] >= 210.0:
            race_over = True
            winner = color[turtles.index(turtle)]
            break

if turtle_bet.lower() == winner.lower():
    print("Nice bet. The winner is {w}".format(w=winner))
else:
    print("Sorry. The winner is {w}".format(w=winner))

screen.exitonclick()
