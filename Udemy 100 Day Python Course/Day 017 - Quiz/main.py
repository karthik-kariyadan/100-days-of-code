from question_model import Question
from quiz_brain import QuizBrain
from requests import get
from html import unescape

categories = [
    "Any Category",
    "General Knowledge",
    "Entertainment: Books",
    "Entertainment: Film",
    "Entertainment: Music",
    "Entertainment: Musicals & Theatres",
    "Entertainment: Television",
    "Entertainment: Video Games",
    "Entertainment: Board Games",
    "Science & Nature",
    "Science: Computers",
    "Science: Mathematics",
    "Mythology",
    "Sports",
    "Geography",
    "History",
    "Politics",
    "Art",
    "Celebrities",
    "Animals",
    "Vehicles",
    "Entertainment: Comics",
    "Science: Gadgets",
    "Entertainment: Japanese Anime & Manga",
    "Entertainment: Cartoon & Animations",
]

while True:
    num_of_questions = int(input("Enter the number of questions you want in the quiz (1-50): "))

    if 1 <= num_of_questions <= 50:
        break
    else:
        print("The number of questions must be between 1 and 50.\n")

while True:
    category = input(f"\nEnter the category you want from: \n\n{"\n".join(categories)}\n\n").title()

    if category in categories:
        break
    else:
        print("\nCategory must be exactly typed as in the list above.")

while True:
    difficulty = input("\nEnter the difficulty ('any difficulty'/'easy'/'medium'/'hard'): ").lower()

    if difficulty in ["any difficulty", "easy", "medium", "hard"]:
        break
    else:
        print("Invalid difficulty.")

url = f"https://opentdb.com/api.php?amount={num_of_questions}{"" if category == "any category" else "&category=" + str(categories.index(category) + 8)}{"" if difficulty == "any difficulty" else "&difficulty=" + difficulty}&type=boolean"

question_data = get(url).json()

if question_data["response_code"] != 0:
    print(
        "\nSomething went wrong getting the questions (there most likely wasn't enough questions available). Please try again later or use different settings!"
    )
else:
    question_bank = [Question(unescape(question["question"]), question["correct_answer"]) for question in
                     question_data["results"]]

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print(f"\nYou've completed the quiz!\nYour final score was: {quiz.score}/{len(question_bank)}.")
