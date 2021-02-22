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

        self.total_score = 0
        self.score = Label(text=f"Score {self.total_score}", fg="white", bg=THEME_COLOR)
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
        self.get_next_question()

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_true(self):
        if self.quiz.check_answer('true'):
            self.total_score += 1
            self.score.config(text=f"Score {self.total_score}")
        self.end_quiz()
        self.get_next_question()

    def answer_false(self):
        if self.quiz.check_answer('false'):
            self.total_score += 1
            self.score.config(text=f"Score {self.total_score}")
        self.end_quiz()
        self.get_next_question()

    def end_quiz(self):
        end_statement = f"You've completed the quiz\n" \
                        f"Your final score was: {self.total_score}/{self.quiz.question_number}"
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=end_statement)




