
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.correct = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input('Q' + str(self.question_number) + ': ' + question.text + '(True/False): ')
        if question.answer == user_answer:
            self.correct += 1
        print('Score = {c}/{qn}'.format(c=self.correct, qn=self.question_number))

