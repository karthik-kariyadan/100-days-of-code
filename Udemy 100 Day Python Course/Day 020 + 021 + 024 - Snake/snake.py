from turtle import Turtle

SNAKE_STARTING_LENGTH = 3
SNAKE_PIECE_SPACING = 20
SNAKE_MOVEMENT_DIST = 20

SNAKE_HEAD_COLOR = "forest green"
SNAKE_BODY_COLOR_1 = "lime green"
SNAKE_BODY_COLOR_2 = "lawn green"

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.head: Turtle = Turtle()

        self.create_snake()

    def create_snake(self) -> None:
        for i in range(SNAKE_STARTING_LENGTH):
            self.add_segment((SNAKE_PIECE_SPACING * -1 * i, 0))

        self.head = self.segments[0]
        self.head.color(SNAKE_HEAD_COLOR)

    def add_segment(self, position: tuple[int, int]):
        starting_segment = Turtle()
        starting_segment.shape("square")
        starting_segment.color(
            SNAKE_HEAD_COLOR if len(self.segments) == 0 else (
                SNAKE_BODY_COLOR_1 if self.segments[-1].color()[0] == SNAKE_BODY_COLOR_2
                else SNAKE_BODY_COLOR_2
            )
        )
        starting_segment.speed(0)
        starting_segment.penup()
        starting_segment.goto(position)

        self.segments.append(starting_segment)

    def move(self) -> None:
        for segment_index in range(len(self.segments) - 1, 0, -1):
            previous_segment = self.segments[segment_index - 1]
            self.segments[segment_index].goto((previous_segment.xcor(), previous_segment.ycor()))

        self.head.forward(SNAKE_MOVEMENT_DIST)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        for segment in self.segments:
            segment.hideturtle()

        self.segments = []

        self.create_snake()
