from turtle import Turtle

SCORE_Y = 250
SCORE_FONT = ("ArcadeClassic", 50, "bold")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, SCORE_Y)

        self.left_score = 0
        self.right_score = 0

        self.score_text = ""

    def draw_score(self) -> None:
        self.clear()

        self.score_text = f"{self.left_score} – {self.right_score}"
        self.write(self.score_text, False, "center", SCORE_FONT)
