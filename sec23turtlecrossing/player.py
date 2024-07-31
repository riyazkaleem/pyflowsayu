#importing turtle modules
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    #defining the player constructor
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color('blue')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y

    #defining the up function
    def up(self):
        y_new = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(), y_new)

    #refreshing the player position
    def player_refresh(self):
        self.goto(STARTING_POSITION)

    
    
