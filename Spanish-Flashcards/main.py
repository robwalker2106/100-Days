from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

title_text = "Title"
word_text = "Word"

word_df = pandas.read_csv("./data/spanish_words_1k.csv")
word_list = word_df.







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

card_title = canvas.create_text(400, 150, text=title_text, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=word_text, font=("Arial", 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
right = Button(image=right_img, highlightthickness=0)
wrong = Button(image=wrong_img, highlightthickness=0)
wrong.grid(row=1, column=0)
right.grid(row=1, column=1)



window.mainloop()


