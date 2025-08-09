from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

position1 = (350, 0)
position2 = (-350, 0)

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle(position1)
paddle2 = Paddle(position2)
ball = Ball()
sc_board = ScoreBoard()

screen.listen()
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380 :
        ball.reset_position()
        sc_board.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        sc_board.r_point()
screen.exitonclick()