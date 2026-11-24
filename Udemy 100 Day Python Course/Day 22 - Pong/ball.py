from paddle import Paddle
from turtle import Turtle
from math import sqrt, copysign
from random import choice

STARTING_DX = 3
STARTING_DY = 3

STRETCH_LENGTH: float | int = 0.75
STRETCH_WIDTH: float | int = 0.75

MINIMUM_X_COR = 269
MAXIMUM_X_COR = 271
MINIMUM_Y_COR = -280
MAXIMUM_Y_COR = 289


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=STRETCH_LENGTH, stretch_wid=STRETCH_WIDTH)
        self.penup()
        self.speed(0)
        self.home()

        self.dx = 0
        self.dy = 0
        self.ball_speed = 0

        self.initialise_speed_and_direction()

    def initialise_speed_and_direction(self) -> None:
        self.ball_speed = 1
        self.dx = STARTING_DX * choice([-1, 1]) * self.ball_speed
        self.dy = STARTING_DY * choice([-1, 1]) * self.ball_speed

    def move(self) -> None:
        self.setx(self.xcor() + (self.dx * self.ball_speed))
        self.sety(self.ycor() + (self.dy * self.ball_speed))

    def bounce_paddle(self, paddle: Paddle) -> None:
        if self.xcor() < 0:
            self.setx(-1 * MINIMUM_X_COR)
        else:
            self.setx(MINIMUM_X_COR)

        offset = (self.ycor() - paddle.ycor()) / ((paddle.stretch_width * 20) / 2)
        offset = max(-0.8, min(0.8, offset))

        speed = sqrt(self.dx ** 2 + self.dy ** 2)

        self.dx = -1 * copysign(sqrt(speed ** 2 - (offset * speed) ** 2), self.dx)
        self.dy = offset * speed

    def bounce_wall(self) -> None:
        if self.ycor() < 0:
            self.sety(MINIMUM_Y_COR)
        else:
            self.sety(MAXIMUM_Y_COR)

        self.dy *= -1

    def check_collision_with_wall(self) -> bool:
        if self.ycor() <= MINIMUM_Y_COR or self.ycor() >= MAXIMUM_Y_COR:
            return True

        return False

    def check_collision_with_paddle(self, paddle: Paddle) -> bool:
        paddle_width: float | int = 20 * paddle.stretch_width

        at_appropriate_xcor: bool = (
                abs(self.xcor() - paddle.xcor())
                <= (10 * STRETCH_LENGTH) + ((20 * paddle.stretch_length) / 2)
        )

        at_appropriate_ycor: bool = (
                (paddle.ycor() - (paddle_width / 2) - 5)
                <= self.ycor() <=
                (paddle.ycor() + (paddle_width / 2) + 5)
        )

        return at_appropriate_xcor and at_appropriate_ycor
