from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
image = canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 130, text="oo:oo", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer_text.grid(column=1, row=0)

start_button = Button(text="Start", fg=GREEN, bg=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=GREEN, bg=YELLOW)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark.grid(column=1, row=3)



window.mainloop()