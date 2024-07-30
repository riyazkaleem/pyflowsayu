#importing modules
from turtle import Turtle

#creating a paddle class
class Ball(Turtle):

    #constructor for ball class
    def __init__(self):
        #calling the turtle super class
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('white')
        self.goto(0,0)
        self.xmove=1
        self.ymove=1

    def ball_move(self):
        x1=self.xcor()+self.xmove
        y1=self.ycor()+self.ymove
        self.goto(x1, y1)
    
    def bounce(self):
        self.ymove *= -1

    def bouncepaddle(self):
        self.xmove *= -1