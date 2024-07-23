#importing modules
from turtle import Turtle

#creating a paddle class
class Paddle(Turtle):
    
    #constructor for paddle class
    def __init__(self):
        #calling the turtle super class
        super().__init__()
        self.right_paddle()
        self.left_paddle()

    #declaring the right paddle
    def right_paddle(self):
        rpad=self.shape("square")
        rpad.penup()
        rpad.color('white')
        rpad.shapesize(stretch_len=1, stretch_wid=5)
        rpad.goto(350,0)

    #declaring the left paddle
    def left_paddle(self):
        lpad=self.shape("square")
        lpad.penup()
        lpad.color('white')
        lpad.shapesize(stretch_len=1, stretch_wid=5)
        lpad.goto(-350,0)
    
    #defining paddle up function
    def up(self):
        self.setheading(90)

    #defining paddle down function
    def down(self):
        self.setheading(270)
