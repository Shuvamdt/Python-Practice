# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squrtle", "Charmandor" ])
table.add_column("Type",["electric", "water", "fire"])
table.align = "l"
print(table)