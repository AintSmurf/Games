from turtle import Turtle, Screen
import random


class Race:
    def __init__(self) -> None:
        # initilaize list to hold the turtles then create turtles
        self.ls = []
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.screen = Screen()
        self.user_input = ""
        self.set_up_the_turtles()

    def set_up_the_turtles(self):
        # make 6 turtles for the game and fill them with color
        for i in range(6):
            self.t = Turtle(shape="turtle")
            self.t.color(self.colors[i])
            self.ls.append(self.t)
        self.initilizae_the_screen()

    def initilizae_the_screen(self):
        # custmize the screen
        self.screen.setup(width=1200, height=600)
        self.user_input = self.screen.textinput(
            title="Who will win?",
            prompt="Enter a color: \n [red, orange, yellow, green, blue, purple] ",
        )
        print(self.user_input)
        self.go_to_the_starting_point()

    def go_to_the_starting_point(self):
        # get all the turtles to the  starting point
        y1 = 150
        for t in self.ls:
            t.penup()
            t.goto(x=-585, y=y1)
            y1 -= 50
        self.start_the_race()

    def start_the_race(self):
        if self.user_input:
            flag = True
            while flag:
                for t in self.ls:
                    t.forward(random.randint(0, 10))
                    # if the turtle reaches the endline stop the game and print to the console who's the winner
                    if t.xcor() > 575:
                        flag = False
                        self.show_the_winner(t)
        else:
            self.validate()
        self.screen.exitonclick()

    def show_the_winner(self, t):
        # get the first index in tuple then convert it to string
        s = str(t.color()[0])
        if s == self.user_input:
            print(f"The Winner is {s} you're right")
        else:
            print(f"The Winner is {s} you're Wrong")
        confirm = self.screen.textinput("wanna bet again? ", "y -yes n -no")
        if confirm == "y":
            self.clear()
            self.__init__()
        else:
            quit()

    def validate(self):
        # validate user input
        confirm = self.screen.textinput(
            "You need to Guess! ", "Wake up Boy confirm with ok"
        )
        if confirm:
            self.clear()
            self.__init__()
        else:
            self.validate()

    def clear(self):
        self.screen.clear()


if __name__ == "__main__":
    Race()
