# from turtle import Turtle, Screen
#
# don = Turtle()
# my_screen = Screen()
# don.shape('turtle')
# don.color('purple4')
# don.pencolor('red1')
# don.forward(210)
# don.right(90)
# don.pencolor('green3')
# don.forward(60)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikacu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table)
