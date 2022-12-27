from turtle import Screen
from cars import Car, LISTOFCARS
from time import sleep
from player import Player
from score import Score


def main():

    # initilaize screen
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("gray")

    screen.tracer(0)

    # intilaize objects
    c = Car()
    p = Player()
    s = Score()

    screen.listen()

    screen.onkey(p.up, "Up")
    screen.onkey(p.down, "Down")

    flag = True

    while flag:
        sleep(0.1)
        screen.update()

        c.move()
        p.move()

        if c.xcor() > -280:
            c.add_new_car()

        # detect collision with the cars
        for car in LISTOFCARS:
            if car.distance(p) < 18:
                flag = False

        # detect collision with the wall
        if p.ycor() > 380:
            s.update()
            p.restart()
            c.increase_level()

    screen.exitonclick()


if __name__ == "__main__":
    main()
