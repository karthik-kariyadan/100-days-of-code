from turtle import Turtle, colormode
from random import randint

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STRETCH_LENGTH = 2.5
CAR_SPAWN_X = 320
MINIMUM_CAR_SPAWN_X = -300
MAXIMUM_CAR_SPAWN_X = 300
MINIMUM_CAR_SPAWN_Y = -260
MAXIMUM_CAR_SPAWN_Y = 260
CAR_SPACING = 25


class CarManager:
    def __init__(self) -> None:
        self.cars: list[Turtle] = []
        self.move_increment = MOVE_INCREMENT
        self.car_spawn_x = CAR_SPAWN_X
        self.minimum_car_spawn_y = MINIMUM_CAR_SPAWN_Y
        self.maximum_car_spawn_y = MAXIMUM_CAR_SPAWN_Y
        self.car_spacing = 25

    def spawn_new_car(self, position: tuple[float | int, float | int]) -> None:
        car = Turtle()

        car.shape("square")
        car.shapesize(stretch_len=STRETCH_LENGTH)
        car.left(180)

        colormode(255)
        car.color((randint(0, 255), randint(0, 255), randint(0, 255)))

        car.speed(0)
        car.penup()
        car.goto(position)

        self.cars.append(car)

    def spawn_starting_cars(self, num_of_cars: int) -> None:
        for _ in range(num_of_cars):
            self.spawn_new_car((
                randint(MINIMUM_CAR_SPAWN_X, MAXIMUM_CAR_SPAWN_X),
                randint(
                    int(MINIMUM_CAR_SPAWN_Y / self.car_spacing),
                    int(MAXIMUM_CAR_SPAWN_Y / self.car_spacing)
                ) * self.car_spacing
            ))

    def move_cars(self) -> None:
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def next_level(self) -> None:
        ...
