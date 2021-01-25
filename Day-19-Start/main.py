from turtle import Turtle, Screen

don = Turtle()

screen = Screen()


def move_forward():
    don.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
