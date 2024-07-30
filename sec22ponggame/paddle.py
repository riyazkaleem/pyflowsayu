#importing modules
from turtle import Turtle

#creating a paddle class
class Paddle(Turtle):
    
    #constructor for paddle class
    def __init__(self):
        #calling the turtle super class
        super().__init__()
        # self.rpaddle()
        # self.lpaddle()
        
    def rpaddle(self):
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(350,0)
    
    def lpaddle(self):
        self.shape("square")
        self.penup()
        self.color('blue')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(-350,0)
    
    #defining paddle up function
    def up(self):
        y1=self.ycor()+20
        self.goto(self.xcor(),y1)

    #defining paddle down function
    def down(self):
        y1=self.ycor()-20
        self.goto(self.xcor(),y1)
