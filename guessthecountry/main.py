from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
score_board = Turtle()
COUNT = 0
LISTOFCOUNTRIES = []
DATA_DIC = {}


def main():

    screen.title("Guess The Country")
    screen.bgcolor("gray")
    image = "states.gif"
    screen.addshape(image)

    score_board.penup()
    score_board.hideturtle()
    score_board.color("blue")

    extract_data()
    pull_the_names()

    Turtle(image)

    while COUNT != len(DATA_DIC):
        update_score()
        ask_question()

    screen.exitonclick()


def update_score():
    score_board.goto(-20, 350)
    score_board.write(
        f"Score: {COUNT}",
        align="center",
        font=("arial", 30, "bold"),
    )


def ask_question():
    answer = screen.textinput(
        "Guess the state", "Take a Guess! \n type quit to stop the game "
    )
    if answer == "quit":
        quit()
    check_country(answer.lower().title())


def extract_data():
    data = pd.read_csv("50_states.csv")
    for country, x, y in zip(data["state"], data["x"], data["y"]):
        DATA_DIC[country] = (x, y)
    return DATA_DIC


def show_on_the_map(coords, country):
    ct = Turtle()
    ct.hideturtle()
    ct.penup()
    ct.goto(coords[0], coords[1])
    ct.write(country)


def pull_the_names():
    answer = extract_data()
    for country in answer.keys():
        LISTOFCOUNTRIES.append(country)


def check_country(name):
    if name in LISTOFCOUNTRIES:
        score_board.clear()
        global COUNT
        COUNT += 1
        LISTOFCOUNTRIES.remove(name)
        update_score()
        show_on_the_map(DATA_DIC[name], name)


if __name__ == "__main__":
    main()
