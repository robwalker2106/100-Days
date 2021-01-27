from turtle import Screen
from snake import Snake
from food import Food
import time


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)
    game_speed = screen.numinput('Game Speed', 'How fast is this game? 1 - 20 (lowest number is slowest')
    snake = Snake(game_speed)
    food = Food()
    screen.listen()
    screen.onkey(snake.turn_up, 'Up')
    screen.onkey(snake.turn_left, 'Left')
    screen.onkey(snake.turn_down, 'Down')
    screen.onkey(snake.turn_right, 'Right')

    while 0 < 1:
        snake.move()
        screen.update()
        time.sleep(.20)

        if snake.head.distance(food) < 15:
            food.move_food()
            snake.grow()

    screen.exitonclick()