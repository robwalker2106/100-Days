from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time


def create_board():
    board = Turtle()
    board.hideturtle()
    board.speed('fastest')
    board.penup()
    board.goto(-271, 271)
    board.setheading(0)
    board.pendown()
    board.pencolor('blue3')
    board.pensize(10)

    for _ in range(4):
        board.forward(540)
        board.right(90)



def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    create_board()
    screen.tracer(0)
    game_speed = screen.numinput('Game Speed', 'How fast is this game? 1 - 20 (lowest number is slowest')
    snake = Snake(game_speed)
    food = Food()
    score = Score()
    screen.listen()
    screen.onkey(snake.turn_up, 'w')
    screen.onkey(snake.turn_left, 'a')
    screen.onkey(snake.turn_down, 's')
    screen.onkey(snake.turn_right, 'd')

    game_on = True

    while game_on:
        snake.move()
        screen.update()
        time.sleep(.20)

        if snake.head.distance(food) < 15:
            food.move_food()
            snake.grow()
            score.gain_point()
            print(score.amount)

        if snake.head.xcor() <= -260 or snake.head.xcor() >= 260 or snake.head.ycor() >= 260 or snake.head.ycor() <= -260:
            score.game_over()
            game_on = False

        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                game_on = False

    screen.exitonclick()