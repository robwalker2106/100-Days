from turtle import Screen
from snake import Snake
import time


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)
    game_speed = screen.numinput('Game Speed', 'How fast is this game? 1 - 20 (lowest number is slowest')
    snake_body = Snake(game_speed)
    screen.listen()
    screen.onkey(snake_body.turn_up, 'Up')
    screen.onkey(snake_body.turn_left, 'Left')
    screen.onkey(snake_body.turn_down, 'Down')
    screen.onkey(snake_body.turn_right, 'Right')

    while 0 < 1:
        snake_body.move()
        screen.update()
        time.sleep(.20)

    screen.exitonclick()