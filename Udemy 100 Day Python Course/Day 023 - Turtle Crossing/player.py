from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("turtle")
        self.setheading(90)

        self.speed(0)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self) -> None:
        self.forward(MOVE_DISTANCE)

    def next_level(self) -> None:
        self.goto(STARTING_POSITION)
