from turtle import Screen
from snake import create_segment, starting_position

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

# Starting coordinates for the snake.
x, y = 0, 0
snake_body = starting_position(x, y)

print(snake_body)
screen.exitonclick()
