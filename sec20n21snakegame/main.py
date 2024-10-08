#import modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#creating objects
screenu = Screen()

#linking the attributes to the objects
screenu.bgcolor('green')
screenu.setup(height=600, width=600)
screenu.title('my snake game')

#creating a snake, food object from snake class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#initializing the scoreboard
scoreboard.current_score=0

#key bindings arrow keys to snake movement
screenu.listen()
screenu.onkey(snake.up, "Up")
screenu.onkey(snake.down, "Down")
screenu.onkey(snake.left, "Left")
screenu.onkey(snake.right, "Right")

#trying to move the snake
game_is_on = True
while game_is_on:
    screenu.update()
    time.sleep(0.01)

    #calls the move method from the snake class
    snake.move()

    #detecting the colliison of snake head with food
    if snake.segments[0].distance(food) < 15:
        # print('yum yum yum')
        food.refresh()
        snake.extend()
        scoreboard.turtle_write()

    #detecting the collision of snake with the wall
    if (snake.segments[0].xcor() > 280) or (snake.segments[0].ycor() > 280) or (snake.segments[0].xcor() < -280) or (snake.segments[0].ycor() < -280):
        scoreboard.gameover()
        game_is_on = False

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

#final screen method for exit on click
screenu.exitonclick()