from turtle import Turtle

SCORE = -1


class Score:
    def __init__(self) -> None:

        # set up the score
        self.txt = Turtle()
        self.txt.hideturtle()
        self.txt.color("blue")
        self.txt.penup()

    def update_the_score(self):
        self.txt.clear()
        global SCORE
        SCORE += 1
        self.txt.setposition(0, 265)
        self.txt.write(
            arg=f"score:{SCORE}",
            move=True,
            align="center",
            font=("arial", 20, "normal"),
        )

    def game_over(self):
        self.gameover = Turtle()
        self.gameover.color("black")
        self.gameover.write(
            arg=f"GAME OVER",
            move=True,
            align="center",
            font=("arial", 40, "bold"),
        )
