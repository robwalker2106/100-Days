from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, move_distance=20):
        self.snake_body = []
        self.move_distance = move_distance
        self.starting_position()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def starting_position(self):

        self.snake_body.append(self.create_segment())
        self.snake_body.append(self.create_segment())
        self.snake_body.append(self.create_segment())

    def create_segment(self):

        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()

        if len(self.snake_body) == 0:
            return turtle
        elif len(self.snake_body) == 1:
            turtle.setheading(self.snake_body[0].heading())
            turtle.goto(self.snake_body[0].position())
            turtle.backward(self.move_distance)
            return turtle
        else:
            turtle.setheading(self.snake_body[-1].heading())
            turtle.goto(self.snake_body[-1].position())
            turtle.backward(20)
            return turtle

    def move(self):
        x, y = self.head.position()

        for i in range(len(self.snake_body)):
            self.snake_body[-i].goto(x, y)

        self.head.forward(self.move_distance)

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
