from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

# Starting coordinates for the snake.
#x, y = 0, 0
snake_body = Snake()

snake_body.starting_position()


# def turn_up():
#     snake_body[0].setheading(90)
#
#
# def turn_left():
#     snake_body[0].setheading(180)
#
#
# def turn_down():
#     snake_body[0].setheading(270)
#
#
# def turn_right():
#     snake_body[0].setheading(0)


screen.onkey(snake_body.turn_up, 'w')
screen.onkey(snake_body.turn_left, 'a')
screen.onkey(snake_body.turn_down, 's')
screen.onkey(snake_body.turn_right, 'd')

while 0 < 1:
    snake_body.move()
    screen.update()
    time.sleep(.1)



screen.exitonclick()
