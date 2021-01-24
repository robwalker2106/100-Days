from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Game is completed. Your final score is {c}/{qn}".format(c=quiz_brain.correct, qn=quiz_brain.question_number))
