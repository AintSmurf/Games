from turtle import Turtle
from random import randint

RIGHT = 0
LEFT = 180


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_ball()
        self.x_move = 18
        self.y_move = 18

    def create_ball(self):
        self.shape("circle")
        self.color("red")
        self.speed(1)
        self.penup()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.xcor() + self.y_move
        self.goto(x, y)

    def reset_position(self):
        self.clear()
        self.goto(0, 0)

    def bounce(self):
        self.y_move *= -1

    def turn_right(self):
        self.y_move *= -1
        self.x_move *= -1

    def turn_left(self):
        self.x_move *= -1
