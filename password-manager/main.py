from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
image = canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_text = Label(text="Website")
website_text.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_username_text = Label(text="Email/Username")
email_username_text.grid(row=2, column=0)

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_text = Label(text="Password")
password_text.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()