from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import randint, shuffle
import requests

question_bank = []
for question in question_data:
    choices = []
    question_text = question.get("question")
    correct_answer = question.get("correct_answer")
    incorrect_answers = question.get("incorrect_answers")
    for ans in incorrect_answers:
        choices.append(ans)
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")