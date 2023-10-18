import requests

import data
from question_model import QuestionModel
from quiz_brain import QuizBrain

choice = input('Please choose the data source. \n- Enter 1 for Data \n- Enter 2 for API \n: ')

if choice == '1':
    print('... Loading questions from Data')

    data_source = data.question_data
    key = 'text'
    value = 'answer'

elif choice == '2':
    print('... Loading questions from API')

    # request API
    url = 'https://opentdb.com/api.php?amount=10'
    response = requests.get(url)
    data_api = response.json()

    data_source = data_api['results']
    key = 'question'
    value = 'correct_answer'

else:
    print('Invalid choice!')
    exit()

# create question list
questions = []
for i in range(len(data_source)):
    question = data_source[i][key]
    answer = data_source[i][value]
    questions.append(QuestionModel(question, answer))

# add questions
quiz_brain = QuizBrain(questions)

# ask a question
while quiz_brain.has_more_question():
    quiz_brain.ask_question()

# finish the quiz
print(f'You\'ve completed the quiz!')
print(f'Your final score was: {quiz_brain.your_score}/{quiz_brain.number}')
