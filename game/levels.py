import json


def get_questions():
    questions = json.load(open('./game/assets/questions/questions.json'))
    return questions
