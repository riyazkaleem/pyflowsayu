#import modules
from turtle import Turtle, Screen
from snake import Snake
import time

#creating objects
screenu = Screen()

#linking the attributes to the objects
screenu.bgcolor('green')
screenu.setup(height=600, width=600)
screenu.title('my snake game')

#creating a snake object from snake class
snake = Snake()

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
    time.sleep(0.1)
    # for obj in segments:
    #     obj.forward(20)

    #calls the move method from the snake class
    snake.move()

#final screen method for exit on click
screenu.exitonclick()