from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
screen.update()
screen.listen()

game_on = True
screen.onkey(l_paddle.move_wall_up, 'w')
screen.onkey(l_paddle.move_wall_down, 's')
screen.onkey(r_paddle.move_wall_up, 'Up')
screen.onkey(r_paddle.move_wall_down, 'Down')

while game_on:
    time.sleep(.1)
    ball.move_ball()

    if 300 <= ball.ycor() or ball.ycor() <= -300:
        ball.change_direction()
    screen.update()



screen.exitonclick()
