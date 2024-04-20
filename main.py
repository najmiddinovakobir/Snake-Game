from turtle import Turtle, Screen, textinput
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

food = Food()
screen = Screen()
writer = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

name = textinput("Game Level", "Easy / Medium / Hard").lower()

snake = Snake()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    if name == "easy":
        time.sleep(0.2)
    elif name == "medium":
        time.sleep(0.1)
    else:
        time.sleep(0.08)
    snake.move()
    writer.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        writer.increase_score()

    if 280 < snake.head.xcor() or -280 > snake.head.xcor() or 280 < snake.head.ycor() or -280 > snake.head.ycor():
        game_is_on = False
        screen.clear()
        writer.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            writer.game_over()

screen.exitonclick()
