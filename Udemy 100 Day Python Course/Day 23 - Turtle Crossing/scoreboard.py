from turtle import Turtle

FONT = ("ArcadeClassic", 30, "bold")
TEXT_X = -230
TEXT_Y = 260


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.color("black")
        self.hideturtle()

        self.speed(0)
        self.goto(TEXT_X, TEXT_Y)

        self.level = 1

        self.write_level()

    def write_level(self) -> None:
        self.clear()

        self.write(f"Level: {self.level}", False, "center", FONT)
