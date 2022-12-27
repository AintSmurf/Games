from turtle import Turtle


class Score(Turtle):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.count = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.shape()
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.hideturtle()

    def intilaize_scoreboard(self, x, y):
        self.setposition(x, y)
        self.write(
            arg=self.count,
            move=True,
            align="center",
            font=("arial", 20, "bold"),
        )

    def update(self, x, y):
        self.clear()
        self.count += 1
        self.intilaize_scoreboard(x, y)
