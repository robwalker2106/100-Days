from turtle import Turtle, Screen
from states import States
from score import Score

screen = Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)
screen.setup(width=900, height=900)
states_map = Turtle(image)
states = States()
score = Score()


while score.score < 50:
    screen.update()

    guess = screen.textinput("Input the name of a state.", " ")
    print(guess.title())

    if guess.lower() == 'exit':
        break

    if guess.title() in states.state_dic.keys():
        states.name_found(guess)
        score.add_point()

states.review()
screen.exitonclick()

