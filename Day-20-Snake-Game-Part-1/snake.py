from turtle import Turtle


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
    :return: List of Turtle() objects.
    """
    start_x = a
    start_y = b
    snake_body = []

    for i in range(3):
        snake_body.append(create_segment(start_x, start_y))
        start_x -= 20

    return snake_body


def move_snake(snake_body):
    """
    Receives the list of Turtle() objects and move all of them by 5 paces.
    :param snake_body: List of Turtle() objects
    :return: None
    """

    for segment in snake_body:
        segment.forward(5)


