from turtle import Turtle

UP = 90
DOWN = 270


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.create_turtle()

    def create_turtle(self):
        self.shapesize(1.5, 1.5)
        self.color("purple")
        self.penup()
        self.goto(0, -380)
        self.setheading(UP)

    def restart(self):
        self.goto(0, -380)

    def move(self):
        self.forward(5)

    def up(self):
        self.setheading(UP)

    def down(self):
        self.setheading(DOWN)
