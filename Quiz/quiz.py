class StartQuiz:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {question.question}: (True/False)? -> ")
        if user_answer == "end":
            self.question_number = 12
            self.still_has_questions()
        else:
            self.check_answer(user_answer, question.answer)

    def check_answer(self,u_ans, answer):

        if u_ans == answer:
            print("You got it right!")
            print(f"It's {answer}")
            self.score += 1
            print(f"Your Score is ({self.score}/{self.question_number})")
        else:
            print("Oops..It's Wrong!")
            print(f"The answer is {answer}")
            print(f"Your Score is ({self.score}/{self.question_number})")



