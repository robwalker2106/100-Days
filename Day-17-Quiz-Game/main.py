from question_model import Question
import data
from quiz_brain import QuizBrain

question_bank = []

for i in data.video_games_easy:
    question_bank.append(Question(i['question'], i['correct_answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You completed the quiz. Your final score is {c}/{qn}".format(c=quiz_brain.correct, qn=quiz_brain.question_number))
