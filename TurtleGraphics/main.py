from turtle import Turtle,Screen
import random
import turtle

turtle.colormode(255)
def set_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
timmy = Turtle()
timmy.color("sea green")
timmy.speed(0)


#colors = ["blue", "navy", "light blue", "cyan", "aquamarine", "sea green", "light green", "lime green", "lime", "dark khaki", "yellow", "saddle brown", "dark orange", "firebrick", "tomato", "red", "pink", "deep pink", "purple", "magenta", "dark violet", "indigo", "slate blue"]

# paths = [0, 90, 180, 270]
# while True:
#     direction = random.choice(paths)
#     timmy.pencolor(set_colors())
#
#     timmy.forward(20)
#     timmy.setheading(direction)

for i in range(0, 120):
    timmy.pencolor(set_colors())
    timmy.right(3)
    timmy.circle(100)
    # for j in range(0, 60):
    #     timmy.forward(6)
    #     timmy.right(6)

screen = Screen()
screen.exitonclick()