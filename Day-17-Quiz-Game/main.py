from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    for q, a in i.items():
        question_bank.append(Question(q, a))

print(question_bank)
