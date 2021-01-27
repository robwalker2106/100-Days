from turtle import Screen
from snake import create_segment, starting_position, move_snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Starting coordinates for the snake.
x, y = 0, 0
snake_body = starting_position(x, y)

print(snake_body)

while 0 < 1:
    move_snake(snake_body)
    screen.update()
    time.sleep(.1)


screen.exitonclick()
