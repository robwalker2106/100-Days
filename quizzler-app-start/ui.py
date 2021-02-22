from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Blank',
            fill=THEME_COLOR,
            font=QUESTION_FONT,
            width=290)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # self.get_next_question()

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.end_quiz()
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_true(self):
        if self.quiz.check_answer('true'):
            self.score.config(text=f"Score {self.quiz.score}")
            self.check_answer(True)
        else:
            self.check_answer(False)

    def answer_false(self):
        if self.quiz.check_answer('false'):
            self.score.config(text=f"Score {self.quiz.score}")
            self.check_answer(True)
        else:
            self.check_answer(False)

    def check_answer(self, ans):
        if ans:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')

        self.window.after(1000, self.get_next_question)

    def end_quiz(self):
        self.canvas.configure(bg='white')
        end_statement = "You've completed the quiz"
        if not self.quiz.still_has_questions():
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text=end_statement)




