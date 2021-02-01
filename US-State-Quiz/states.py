import csv
from turtle import Turtle

FONT = ('Courier', 10, 'normal')


class States:
    def __init__(self):
        self.state_dic = {}
        self.state_names = []

        with open('50_states.csv') as state_file:
            file_data = csv.reader(state_file)
            for line in file_data:
                if line[1] != 'x':
                    self.state_dic[line[0]] = (int(line[1]), int(line[2]))

    def name_found(self, name):
        correct = name.title()
        new_state = Turtle()
        new_state.penup()
        new_state.goto(self.state_dic[correct])
        new_state.pencolor("black")
        new_state.hideturtle()
        new_state.write(correct, FONT)


