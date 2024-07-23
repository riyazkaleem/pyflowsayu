#importing modules
from turtle import Turtle, Screen
from paddle import Paddle

#creating objects
screenu = Screen()
rpaddlu = Paddle()

#setting up screen characteristics
screenu.bgcolor('green')
screenu.title('les play pong !!')
screenu.setup(width=800, height=600)

#key bindings arrows to paddles
screenu.listen()
screenu.onkey(rpaddlu.up, 'Up')
screenu.onkey(rpaddlu.down, 'Down')

#screen ending function
screenu.exitonclick()