from turtle import Turtle, Screen

don = Turtle()

screen = Screen()


def move_forward():
    don.forward(10)


def move_backward():
    don.backward(10)


def clockwise():
    don.setheading(don.heading() + 10)


def counterclockwise():
    don.setheading(don.heading() - 10)


def clear():
    don.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
