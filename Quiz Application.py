#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the level of Lake Urmia?\n(a) 120 meters\n(b) 100 meters\n(c) 135 meters\n\n",
    "Which category of languages does Python belong to?\n(a) programming languages\n(b) debugging languages\n(c) both\n\n",
    "Which city is the capital of Iran?\n(a) Tabriz\n(b) Mashhad\n(c) Tehran\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        print("--------------------------------------------------")
        if answer == question.answer:
            score += 1
    print("You answered {} of {} questions correctly.".format(score, len(questions)))

run_quiz(questions)

