import turtle
from turtle import Turtle, Screen

timmy = Turtle()

def w_forward():
    turtle.forward(10)
def s_backward():
    turtle.backward(10)
def a_counter_clockwise():
    turtle.left(10)
def d_clockwise():
    turtle.right(10)
def c_clear():
    turtle.reset()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=w_forward)
screen.onkey(key="s", fun=s_backward)
screen.onkey(key="a", fun=a_counter_clockwise)
screen.onkey(key="d", fun=d_clockwise)
screen.onkey(key="c", fun=c_clear)
screen.exitonclick()