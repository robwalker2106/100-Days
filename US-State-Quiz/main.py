from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
states = Turtle(image)


screen.exitonclick()