from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.intilaize_scoreboard()

    def intilaize_scoreboard(self):
        self.goto(-20, 350)
        self.write(
            f"LEVEL: {self.level}",
            align="center",
            font=("arial", 30, "bold"),
        )

    def update(self):
        self.clear()
        self.level += 1
        self.intilaize_scoreboard()
