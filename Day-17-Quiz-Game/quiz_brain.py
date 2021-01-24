
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.correct = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input('Q' + str(self.question_number) + ': ' + question.text + '(True/False): ')
        self.check_answer(question, user_answer)
        print('Your current score is: {c}/{qn}.\n'.format(c=self.correct, qn=self.question_number))

    def check_answer(self, question, user_answer):
        if question.answer.lower() == user_answer.lower() or question.answer.lower()[0] == user_answer.lower()[0]:
            self.correct += 1
            print("You got it right!")
        else:
            print("Sorry, that was incorrect.")
        print("The correct answer was: {a}.".format(a=question.answer))
