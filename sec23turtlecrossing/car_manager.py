#importing turtle modules
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    #defining the car manager constructor
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(COLORS[1])
        self.shapesize(stretch_len=1, stretch_wid=2)
        self.goto(300,0)

    #creating a car moving from right to left
    def car_movement(self):
        x_new = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(x_new, self.ycor())

    #def refreshing the car movement
    def car_refresh(self):
        self.goto(300,0)
