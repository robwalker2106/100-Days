from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITION = [0, 0]


class Snake:
    def __init__(self):
        self.x_start = START_POSITION[0]
        self.y_start = START_POSITION[1]
        self.snake_body = []
        self.starting_position()
        self.head = self.snake_body[0]

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
        x, y = self.head.position()

        for i in range(len(self.snake_body)):
            self.snake_body[-i].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        self.head.setheading(90)

    def turn_left(self):
        self.head.setheading(180)

    def turn_down(self):
        self.head.setheading(270)

    def turn_right(self):
        self.head.setheading(0)
