from turtle import Turtle
MOVE_DISTANCE = 20
START_POSITION = [0, 0]

class Snake:
    def __init__(self):
        self.x_start = START_POSITION[0]
        self.y_start = START_POSITION[1]
        self.snake_body = []

    def starting_position(self):

        for i in range(3):
            self.snake_body.append(self.create_segment(self.x_start, self.y_start))
            self.x_start -= 20

    def create_segment(self, x, y):

        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(x, y)

        return turtle

    def move(self):
        x, y = self.snake_body[0].position()

        for i in range(len(self.snake_body)):
            self.snake_body[-i].goto(x, y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def turn_up(self):
        self.snake_body[0].setheading(90)

    def turn_left(self):
        self.snake_body[0].setheading(180)

    def turn_down(self):
        self.snake_body[0].setheading(270)

    def turn_right(self):
        self.snake_body[0].setheading(0)

# def create_segment(x, y):
#     """
#     Receives an x and y coordinate and creates a segment for the snake body.
#     :param x: int
#     :param y: int
#     :return: Turtle() object
#     """
#     turtle = Turtle(shape='square')
#     turtle.color('white')
#     turtle.penup()
#     turtle.goto(x, y)
#     return turtle


# def starting_position(a, b):
#     """
#     Creates the starting position for the snake starting with three segments.
#     :param a: int
#     :param b: int
#     :return: List of Turtle() objects.
#     """
#     start_x = a
#     start_y = b
#     snake_body = []
#
#     for i in range(3):
#         snake_body.append(create_segment(start_x, start_y))
#         start_x -= 20

    # return snake_body


# def move_snake(snake_body):
#     """
#     Receives the list of Turtle() objects and move all of them by 20 paces.
#     :param snake_body: List of Turtle() objects
#     :return: None
#     """
#     x, y = snake_body[0].position()
#
#     for i in range(len(snake_body)):
#         snake_body[-i].goto(x, y)
#
#     snake_body[0].forward(20)
