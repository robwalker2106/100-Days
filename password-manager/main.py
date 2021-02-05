from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import  pyperclip

lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", " "]

upper_letters = [x.upper() for x in lower_letters]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "$", "%", "&", "#", "^", "[", "]"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    lower_letters_int = randint(5, 7)
    upper_letters_int = randint(2, 4)
    numbers_int = randint(2, 4)
    symbols_int = randint(2, 4)

    password = [choice(lower_letters) for _ in range(lower_letters_int)]
    password += [choice(upper_letters) for _ in range(upper_letters_int)]
    password += [choice(numbers) for _ in range(numbers_int)]
    password += [choice(symbols) for _ in range(symbols_int)]

    shuffle(password)

    password_string = ""

    for char in password:
        password_string += char

    print(password_string)

    password_entry.delete(0, END)
    password_entry.insert(0, password_string)
    pyperclip.copy(password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    username = email_username_entry.get()
    password = password_entry.get()
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    message_string = 'Do you want to save the following:\nWebsite: {website}\nPassword: {password}'.format(website=website, username=username, password=password)

    if len(password) < 8:
        messagebox.showerror(title="Password Length",
                             message="Password entered is too short. Must be at least 8 characters.")
        save = False
    elif website == "":
        messagebox.showerror(title="Website Name", message="Please enter a valid website name.")
        save = False
    else:
        save = messagebox.askokcancel(title=website, message=message_string)

    if save:
        with open('passwords.txt', 'a') as file:
            file.write(website + " | " + username + " | " + password + "\n")


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
website_entry.focus()

email_username_text = Label(text="Email/Username")
email_username_text.grid(row=2, column=0)

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'username@email.com')

password_text = Label(text="Password")
password_text.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
