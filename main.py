import data
from question_model import QuestionModel
from quiz_brain import QuizBrain

# create question list
questions = []
for i in range(len(data.question_data)):
    text = data.question_data[i]['text']
    answer = data.question_data[i]['answer']
    questions.append(QuestionModel(text, answer))
quiz_brain = QuizBrain(questions)

while quiz_brain.has_more_question():
    quiz_brain.ask_question()  # ask a question

# finish the quiz
print(f'You\'ve completed the quiz!')
print(f'Your final score was: {quiz_brain.your_score}/{quiz_brain.number}')
