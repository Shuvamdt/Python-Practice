from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
set_y = -90
turtles = []
is_bet_done = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle is going to win? :")

if user_bet :
    is_bet_done = True

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=set_y)
    set_y+=30
    turtles.append(new_turtle)

while is_bet_done:
    for turt in turtles:
        if turt.xcor() > 230:
            winner = turt.pencolor()
            is_bet_done = False
            if winner == user_bet:
                print(f"You've won ! The {winner} turtle won!")
            else:
                print(f"You've lost ! The {winner} turtle won!")
        turt.forward(random.randint(0, 10))
screen.exitonclick()