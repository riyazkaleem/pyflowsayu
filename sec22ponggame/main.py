#importing modules
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#creating objects
screenu = Screen()
screenu.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
paddle1.rpaddle()
paddle2.lpaddle()

ball = Ball()
scoreboard = Scoreboard()
#setting up screen characteristics
screenu.bgcolor('green')
screenu.title('les play pong !!')
screenu.setup(width=800, height=600)

#key bindings arrows to paddles
screenu.listen()
screenu.onkey(paddle1.up, 'Up')
screenu.onkey(paddle1.down, 'Down')
screenu.onkey(paddle2.up, 'w')
screenu.onkey(paddle2.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screenu.update()
    ball.ball_move()

    #detect collision with top boundary of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        print('touched boundary')
        ball.bounce()

    #detect collision with the right paddle
    if ball.xcor() >330 and ball.distance(paddle1)<50:
        print('paddle touched')
        ball.bouncepaddle()
        scoreboard.rpoint()

    elif ball.xcor() >360 and ball.distance(paddle1)>40:
        print('point loss')
        ball.goto(0,0)
        ball.bounce()
        ball.bouncepaddle()

    #detect collision with the left paddle
    if ball.xcor() <-330 and ball.distance(paddle2)<50:
        print('paddle touched')
        ball.bouncepaddle()
        scoreboard.lpoint()

    elif ball.xcor() <-360 and ball.distance(paddle2)>40:
        print('point loss')
        ball.goto(0,0)
        ball.bounce()
        ball.bouncepaddle()

#screen ending function
screenu.exitonclick()