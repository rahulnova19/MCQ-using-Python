class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Lists are mutable or not?\n(a) 'yes'\n(b)'no'\n(c)'cant say'", '\n'
                                                         "Which of them have key value pairs?\n(a) 'list'\n(b)'tuple'\n(c)'dict'", '\n'
                                                                                                               "Strings are of which type?\n (a) 'mutable'\n (b) 'immutable'\n(c)'cant say'",
    '\n'
    "Does set type allow duplicate elements ?\n (a) 'yes'\n (b) 'no'\n(c)'cant say", '\n'
                                                              "Tuples are of what type?\n (a) 'immutable'\n (b) 'mutable'\n(c)'cant say'",
    '\n'
]
name = input("Please enter your name: ").title()
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\n{0}, you scored {1} out of {2}.".format(name, score, len(questions)))


run_quiz(questions)