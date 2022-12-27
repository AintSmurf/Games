from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()

        # coords to randomize the food
        self.width = (-575, 575)
        self.height = (-275, 275)

    def add_food(self):
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(
            random.randint(self.width[0], self.width[1]),
            random.randint(self.height[0], self.height[1]),
        )
        self.showturtle()

    def remove_food(self):
        self.hideturtle()
