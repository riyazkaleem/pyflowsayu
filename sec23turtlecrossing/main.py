import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#creating a player, car object
player = Player()
car = CarManager()
sboard = Scoreboard()

#creating key bindings for turtle crossing
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #checking if the player reached the top goal
    if player.ycor() >= player.finish_line:
        print('game level done')
        player.player_refresh()
        sboard.increase_level()
        sboard.update_scoreboard()

    car.create_car()
    car.move_cars()

    #detecting turtle collision with car
    for acar in car.all_cars:
        if acar.distance(player) < 30:
            print('car collided with turtle')
            sboard.game_over()
            game_is_on = False


screen.exitonclick()