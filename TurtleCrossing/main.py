import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
sb = Scoreboard()
car_manager = CarManager()

game_is_on = True
screen.listen()
screen.onkey(player.move, "w")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    if player.check_end_point():
        sb.level_up()
        car_manager.speed_up()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            sb.game_over()

screen.exitonclick()