from turtle import Turtle

SCORE_FONT = ("ArcadeClassic", 30, "bold")
GAME_OVER_FONT = ("ArcadeClassic", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, 270)

        self.score = 0

        with open("high_score.txt", "r") as high_score:
            self.high_score = int(high_score.read())

        self.draw_score()

    def draw_score(self) -> None:
        self.clear()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", False, "center", SCORE_FONT)

    def increase_score(self) -> None:
        self.score += 1

        if self.score > self.high_score:
            self.high_score += 1

            with open("high_score.txt", "w") as high_score:
                high_score.write(str(self.high_score))

        self.draw_score()

    def reset(self) -> None:
        self.score = 0
        self.draw_score()

    def game_over(self) -> None:
        self.home()
        self.color("dark red")
        self.write("GAME OVER", False, "center", GAME_OVER_FONT)
