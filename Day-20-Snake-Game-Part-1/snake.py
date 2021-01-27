from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITION = [0, 0]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
