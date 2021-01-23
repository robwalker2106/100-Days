from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

quiz_brain = QuizBrain(question_bank)

start = 0

while start <= len(question_bank):
    question = quiz_brain.next_question()
    correct = question.answer
    answer = input('Q' + str(quiz_brain.question_number) + '. ' + question.text + '(True/False): ')
    print(correct == answer)
