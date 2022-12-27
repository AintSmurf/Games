from turtle import Turtle
from random import randint


LISTOFCARS = []


class Car(Turtle):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.default_speed = 5
        self.flag = 20
        self.hideturtle()
        self.add_new_car()
        self.currentcar = LISTOFCARS[0]

    def add_new_car(self):
        if len(LISTOFCARS) != self.flag:
            car = Turtle()
            car.shape("turtle")
            car.color(self.colors[randint(0, len(self.colors) - 1)])
            car.shapesize(1.5, 2)
            car.penup()
            car.goto(-380, randint(-380, 380))
            LISTOFCARS.append(car)

    def move(self):
        for car in LISTOFCARS:
            car.forward(self.default_speed)

    def increase_level(self):
        self.default_speed += 5
        self.flag += 20
        self.add_new_car()
