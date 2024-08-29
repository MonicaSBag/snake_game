from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Lavender")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
text = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        text.increase_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        text.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            text.reset()
            snake.reset()

screen.exitonclick()
