from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
image = canvas.create_image(100, 100, image=lock_image)
canvas.pack()

window.mainloop()