from data import question_data
from question_model import Question
from quiz import StartQuiz
from logo import logo

print(logo)

question_bank = []

for question in question_data:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text,answer)
    question_bank.append(new_question)

print("If you want to End the quiz Type('end')")
quiz = StartQuiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your Final Score is {quiz.score}/{quiz.question_number}")