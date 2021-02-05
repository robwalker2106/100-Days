from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
sessions = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global sessions
    global timer
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    sessions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(WORK_MIN * 60)


def short_break():
    timer_label.config(text="Break Time")
    count_down(SHORT_BREAK_MIN * 60)


def long_break():
    timer_label.config(text="Rest Period")
    count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global sessions
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text="{}:{}".format(count_min, count_sec))

    if count > 0:
        window.after(1000, count_down, count - 1)
    elif count == 0 and sessions < 4:
        global timer
        timer = window.after(1000, short_break)
        sessions += 1
        check_mark.config(text="✓" * sessions)
    else:
        window.after(1000, long_break)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
image = canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="oo:oo", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", fg=GREEN, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=GREEN, bg=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓" * sessions, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark.grid(column=1, row=3)



window.mainloop()