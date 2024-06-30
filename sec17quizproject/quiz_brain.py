
#creating a new question brain class
class QuestionBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_response=input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?:")
        print(user_response)
        self.question_number += 1
        self.check_answer(user_response, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'you go it right, your score is: {self.score}')
        else:
            print('you got it wrong')
            print(f'correct answer: {correct_answer}')

