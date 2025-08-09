import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
writer = Turtle()
data= pandas.read_csv("50_states.csv")

state_list = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

writer.penup()
writer.hideturtle()

guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Current Score: {len(guessed_states)}", prompt="Tell me a states name.")
    if answer_state == "Exit":
        # for i in state_list:
        #     if i not in guessed_states:
        #         missing_states.append(i)
        missing_states = [item for item in state_list if item not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    else:
        if answer_state.title() in state_list:
            guessed_states.append(answer_state.title())
            state_data = data[data.state == answer_state.title()]
            writer.goto(state_data.x.item(), state_data.y.item())
            writer.write(answer_state, False, align="center", font=("Arial", 10, "normal"))
screen.exitonclick()