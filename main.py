import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish():
        scoreboard.level_up()
        car_manager.speed_up()
        player.reset_position()

screen.exitonclick()