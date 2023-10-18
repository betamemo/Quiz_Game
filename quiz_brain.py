from typing import List

from question_model import QuestionModel


class QuizBrain:
    def __init__(self, questions: List[QuestionModel]):
        self.questions = questions
        self.number = 0
        self.your_score = 0

    def has_more_question(self):
        return self.number < len(self.questions)

    def ask_question(self):
        question = self.questions[self.number].text
        answer = self.questions[self.number].answer

        # ask the question
        your_answer = input(f'Q{self.number + 1}. {question} ({answer}): ')
        self.number += 1

        # check the answer
        if answer.upper() == your_answer.upper():
            print('You got it right!')  # if the answer is correct
            self.your_score += 1
        else:
            print(f'The correct answer was: {answer}')  # if the answer is incorrect

        # update the score
        print(f'Your current score was: {self.your_score}/{self.number}\n')
