from turtle import Turtle


class Score:
    def __init__(self) -> None:

        # set up the score
        self.txt = Turtle()
        self.txt.hideturtle()
        self.txt.color("blue")
        self.txt.penup()
        self.score = 0
        self.position_the_score()

    def position_the_score(self):
        self.txt.setposition(0, 265)
        self.txt.write(
            arg=f"score:{self.score}",
            move=True,
            align="center",
            font=("arial", 20, "normal"),
        )

    def update_the_score(self):
        self.txt.clear()
        self.score += 1
        self.position_the_score()

    def game_over(self):
        self.gameover = Turtle()
        self.gameover.color("black")
        self.gameover.write(
            arg=f"GAME OVER",
            move=True,
            align="center",
            font=("arial", 40, "bold"),
        )
