from turtle import Turtle

STRETCH_LENGTH: float | int = 0.5
STARTING_STRETCH_WIDTH: int = 4

MOVEMENT_DISTANCE = 5

STARTING_MAXIMUM_DISTANCE = 245

STARTING_X = 280


class Paddle(Turtle):
    def __init__(self, side: str) -> None:
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=STRETCH_LENGTH, stretch_wid=STARTING_STRETCH_WIDTH)
        self.penup()
        self.speed(0)
        self.goto((-1 * STARTING_X) if side == "left" else STARTING_X, 0)

        self.stretch_length = STRETCH_LENGTH
        self.stretch_width = STARTING_STRETCH_WIDTH
        self.starting_maximum_distance = STARTING_MAXIMUM_DISTANCE
        self.maximum_distance = self.starting_maximum_distance
        self.starting_x = STARTING_X

    def initialise_stretch_width_and_maximum_distance(self) -> None:
        self.stretch_width = STARTING_STRETCH_WIDTH
        self.shapesize(stretch_len=STRETCH_LENGTH, stretch_wid=self.stretch_width)
        self.maximum_distance = self.starting_maximum_distance

    def up(self) -> None:
        if self.ycor() <= self.maximum_distance:
            self.goto(self.xcor(), self.ycor() + MOVEMENT_DISTANCE)

    def down(self) -> None:
        if self.ycor() >= (self.maximum_distance * -1):
            self.goto(self.xcor(), self.ycor() - MOVEMENT_DISTANCE)
