from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, snake: list[Turtle]):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.penup()

        self.refresh(snake)

    def refresh(self, snake: list[Turtle]):
        self.goto(randint(-14, 14) * 20, randint(-14, 14) * 20)

        for segment in snake:
            if (int(segment.pos()[0]), int(segment.pos()[1])) == (self.pos()[0], self.pos()[1]):
                self.refresh(snake)
