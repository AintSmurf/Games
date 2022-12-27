from turtle import Screen
from score import Score
from time import sleep
from paddle import Paddle, DOWN, UP
from ball import Ball


PCCOORDS = [(375, -20), (375, 0), (375, 20)]


def main():
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("gray")
    screen.tracer(0)

    # initilaize objects
    s1 = Score()
    s2 = Score()
    player_paddle = Paddle()
    ball = Ball()
    pc_paddle = Paddle(*PCCOORDS)

    s1.intilaize_scoreboard(50, 365)
    s2.intilaize_scoreboard(-50, 368)

    screen.listen()
    screen.onkey(player_paddle.up, "Up")
    screen.onkey(player_paddle.down, "Down")

    flag = True
    while flag:
        sleep(0.1)
        screen.update()
        player_paddle.move()
        pc_paddle.move()
        ball.move()

        # update scores and reset ball
        if ball.xcor() > 400:
            ball.reset_position()
            ball.turn_left()
            s2.update(-50, 365)
        if ball.xcor() < -400:
            ball.reset_position()
            ball.turn_right()
            s1.update(50, 368)

        # detect collision with wall (top,bottom)
        if ball.ycor() > 380 or ball.ycor() < -380:
            ball.bounce()

        # detect the movement of the pc
        if pc_paddle.head.ycor() < -370:
            pc_paddle.head.setheading(UP)

        if pc_paddle.head.ycor() > 370:
            pc_paddle.head.setheading(DOWN)

        # detect collision with ball
        for s in player_paddle.segments[1:]:
            if s.distance(ball) < 20:
                ball.turn_right()

        # detect collision with ball fo pc
        for s in pc_paddle.segments[1:]:
            if s.distance(ball) < 20:
                ball.turn_left()

    screen.exitonclick()


if __name__ == "__main__":
    main()
