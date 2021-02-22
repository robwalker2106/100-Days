from question_model import Question
from data import QUESTION_DATA, Parameters
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

param_ui = Parameters()

for question in QUESTION_DATA:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    print(question_text)
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
