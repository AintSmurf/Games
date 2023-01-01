from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from time import sleep


def main():

    screen = Screen()
    screen.setup(width=1200, height=600)
    screen.bgcolor("gray")
    screen.tracer(0)

    # initilaize objects
    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # start the game
    flag = True
    food.add_food()
    while flag:
        screen.update()
        sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.remove_food()
            snake.extend()
            food.add_food()
            score.update_the_score()

        # detect collision with wall
        if (
            snake.head.xcor() > 598
            or snake.head.xcor() < -600
            or snake.head.ycor() > 300
            or snake.head.ycor() < -298
        ):
            flag = False
            score.game_over()

        # detect collision with tail
        for s in snake.segments[1:]:
            if snake.head.distance(s) < 15:
                flag = False
                score.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
