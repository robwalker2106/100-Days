from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake_body = Snake()
screen.listen()
screen.onkey(snake_body.turn_up, 'Up')
screen.onkey(snake_body.turn_left, 'Left')
screen.onkey(snake_body.turn_down, 'Down')
screen.onkey(snake_body.turn_right, 'Right')

while 0 < 1:
    snake_body.move()
    screen.update()
    time.sleep(.1)


screen.exitonclick()
