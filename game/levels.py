import json


def get_questions():
    questions = json.load(open('./game/assets/questions/questions.json'))
    return questions

levels = [
    {
        "question": {
            "type":"Text",
            "value":"ahhhhhhhhhh?"
        },
        "answers": [
            {
                "type": "Text",
                "value": "Answer",
                "answer":True
            },
            {
                "type": "Text",
                "value": "Answer 2"
            },
            {
                "type": "Text",
                "value": "Answer 3"
            },
            {
                "type": "Text",
                "value": "Answer 4"
            },
            {
                "type": "Text",
                "value": "Answer 5"
            },
            {
                "type": "Text",
                "value": "Answer 6"
            }
        ]
    },
    {
        "question": {
            "type":"Text",
            "value":"ahhhhhhhhhh?"
        },
        "answers": [
            {
                "type": "Text",
                "value": "Answer",
                "answer":True
            },
            {
                "type": "Text",
                "value": "Answer 2"
            },
            {
                "type": "Text",
                "value": "Answer 3"
            },
            {
                "type": "Text",
                "value": "Answer 4"
            },
            {
                "type": "Text",
                "value": "Answer 5"
            },
            {
                "type": "Text",
                "value": "Answer 6"
            }
        ]
    }
]