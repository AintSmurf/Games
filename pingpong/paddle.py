from turtle import Turtle

PADDLECOORDS = [(-375, -20), (-375, 0), (-375, 20)]
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, *args):
        super().__init__()
        self.segments = []
        if args:
            self.create_paddle(args)
        else:
            self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self, *args):
        if args:
            self.speed(2)
            global PADDLECOORDS
            PADDLECOORDS = args
            list_of_lists = [list(tup) for tup in PADDLECOORDS]
            single = [val for sublist in list_of_lists for val in sublist]
            PADDLECOORDS = single
        self.hideturtle()
        for position in PADDLECOORDS:
            ns = Turtle(shape="square")
            ns.penup()
            ns.goto(position)
            ns.left(90)
            self.segments.append(ns)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)
