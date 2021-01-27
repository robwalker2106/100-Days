from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self, move_distance=20):
        self.snake_body = []
        self.move_distance = move_distance
        self.starting_position()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def starting_position(self):

        for position in POSITION:
            self.create_segment(position)
        print(self.snake_body[-1].pos())

    def create_segment(self, position):

        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.snake_body.append(turtle)

    def grow(self):
        self.create_segment(self.tail.position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

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
