from turtle import Turtle

SNAKESIZE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # build the snake head
        for position in SNAKESIZE:
            self.add_snake(position)

    def extend(self):
        self.add_snake(self.segments[-1].pos())

    def add_snake(self, position):
        ns = Turtle(shape="square")
        ns.penup()
        ns.goto(position)
        self.segments.append(ns)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
