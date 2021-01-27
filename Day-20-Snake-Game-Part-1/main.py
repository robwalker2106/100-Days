from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

# Starting coordinates for the snake.
x, y = 0, 0
snake_body = []


def create_segment(x, y):
    """
    Receives an x and y coordinate and creates a segment for the snake body.
    :param x: int
    :param y: int
    :return: Turtle() object
    """
    turtle = Turtle(shape='square')
    turtle.color('white')
    turtle.penup()
    turtle.goto(x, y)
    return turtle


def starting_position(a, b):
    """
    Creates the starting position for the snake starting with three segments.
    :param a: int
    :param b: int
    :return: None
    """
    start_x = a
    start_y = b

    for i in range(3):
        snake_body.append(create_segment(start_x, start_y))
        start_x -= 20


starting_position(x, y)
print(snake_body)
screen.exitonclick()
