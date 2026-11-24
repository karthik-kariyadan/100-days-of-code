from question_model import Question


class QuizBrain:
    def __init__(self, questions_list: list[Question]) -> None:
        self.question_number: int = 0
        self.score: int = 0
        self.questions_list: list[Question] = questions_list

    def ask_question(self, question_number: int):
        while True:
            user_answer = input(
                f"\nQ.{question_number}: {self.questions_list[question_number - 1].text} (True/False): "
            ).lower()

            if user_answer in ["true", "false"]:
                break
            else:
                print("Please enter a valid answer.")

        return user_answer

    def check_answer(self, user_answer: str) -> bool:
        return user_answer == self.questions_list[self.question_number - 1].answer.lower()

    def next_question(self) -> None:
        self.question_number += 1
        if self.check_answer(self.ask_question(self.question_number)):
            self.score += 1
            print(f"Correct! Current score: {self.score}/{self.question_number}.")
        else:
            print(f"Incorrect! Current score: {self.score}/{self.question_number}.")

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions_list)
