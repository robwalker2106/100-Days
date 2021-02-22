import requests
from tkinter import *

THEME_COLOR = "#375362"
CATEGORIES = ["Entertainment: Film",
              "Entertainment: Video Games",
              "History",
              "Politics",
              "Science: Computers",
              "Science & Nature"
              ]
FONT = ('Arial', 20, 'bold')
CATS = {"Entertainment: Film": 11,
        "Entertainment: Video Games": 15,
        "History": 23,
        "Politics": 24,
        "Science: Computers": 18,
        "Science & Nature": 17}
QUESTION_DATA = []


class Parameters:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.amount_box = Label(text='How many questions do you want?',
                                bg=THEME_COLOR, fg='white', font=FONT)
        self.amount_box.grid(row=0, column=0)
        self.amount_scale = Scale(self.window, from_=1, to=50, orient=HORIZONTAL,
                                  bg=THEME_COLOR, fg='white')
        self.amount_scale.grid(row=0, column=1, padx=10)

        self.categories_label = Label(text='What category do you want to quiz?',
                                      bg=THEME_COLOR, fg='white', font=FONT)
        self.categories_label.grid(row=1, column=0)

        self.default_cat = StringVar()
        self.default_cat.set("Select")
        self.categories = OptionMenu(self.window, self.default_cat, *CATEGORIES)
        self.categories.grid(row=1, column=1)

        self.start = Button(text="Start", command=self.quiz_start)
        self.start.grid(row=2, column=0, columnspan=2)

        self.window.mainloop()

    def quiz_start(self):
        global QUESTION_DATA

        parameters = {
            "amount": self.amount_scale.get(),
            "type": 'boolean',
            "category": CATS[self.default_cat.get()]
        }

        response = requests.get(url='https://opentdb.com/api.php', params=parameters)
        response.raise_for_status()
        response_questions = response.json()
        for question in response_questions['results']:
            QUESTION_DATA.append(question)

        self.window.destroy()






# parameters = {
#     "amount": 10,
#     "type": 'boolean'
# }
#
# response = requests.get(url='https://opentdb.com/api.php', params=parameters)
# response.raise_for_status()
# response_questions = response.json()
#
#question_data = response_questions['results']