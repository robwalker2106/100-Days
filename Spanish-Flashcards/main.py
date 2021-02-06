from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


# ----------------------------------Word List Setup------------------------------------
# ------------------------------------------------------------------------------

try:
    with open('./data/words_to_learn.csv') as file:
        pass
except FileNotFoundError:
    word_df = pandas.read_csv("./data/spanish_words_1k.csv")
    word_list = word_df.to_dict(orient='records')
else:
    word_df = pandas.read_csv("./data/words_to_learn.csv")
    word_list = word_df.to_dict(orient='records')


word_pair = choice(word_list)
print(word_pair)
front_title = "Spanish"
front_word = word_pair[front_title]
back_title = 'English'
back_word = word_pair[back_title]


# ----------------------------------Card Changes------------------------------------
# ------------------------------------------------------------------------------

def next_word():
    global word_pair, flip_timer
    window.after_cancel(flip_timer)
    word_pair = choice(word_list)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(title_text, text="Spanish")
    canvas.itemconfig(word_text, text=word_pair['Spanish'])
    window.after(3000, func=show_back)


def show_back():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=word_pair['English'])


def is_known():
    word_list.remove(word_pair)
    words_to_learn = pandas.DataFrame(word_list)
    words_to_learn.to_csv('./data/words_to_learn.csv', index=False)
    next_word()

# ----------------------------------UI Setup------------------------------------
# ------------------------------------------------------------------------------


window = Tk()
window.title("Spanish Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_img = canvas.create_image(400, 260, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

title_text = canvas.create_text(400, 150, text=front_title, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text=front_word, font=("Arial", 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
right = Button(image=right_img, highlightthickness=0, command=is_known)
wrong = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong.grid(row=1, column=0)
right.grid(row=1, column=1)

flip_timer = window.after(3000, func=show_back)

window.mainloop()



