from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake= Snake()
food = Food()
sc_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sc_board.score_up()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        sc_board.reset()
        snake.reset()
        # game_is_on = False
        # sc_board.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sc_board.reset()
            snake.reset()
            # game_is_on = False
            # sc_board.game_over()
screen.exitonclick()