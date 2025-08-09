import colorgram
import turtle as t
import random

#extracted_colors = colorgram.extract('original_art.jpeg', 30)
colors = [(231, 206, 85), (224, 150, 89), (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38), (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5), (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149), (232, 170, 160), (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175)]
# for i in range (30):
#     rgb_code = (extracted_colors[i].rgb.r, extracted_colors[i].rgb.g, extracted_colors[i].rgb.b)
#     colors.append(rgb_code)
# print(colors)

timmy = t.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed(0)
t.colormode(255)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for i in range (1, 101):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)
    if i %10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(360)


screen = t.Screen()
screen.exitonclick()