#importing turtle class
from turtle import Turtle

#declaring the constants
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
STEP_LENGTH = 20
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_RIGHT = 0
HEADING_LEFT = 180

#creating the snake class
class Snake:
    
    #constructor to create a snake 
    def __init__(self):
        #creating a snake through a default method
        self.create_snake()

    def create_snake(self):
        #creating a snake
        self.segments = []
        # print(chinni.position())
        # print(chinni.turtlesize())
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    #creating a new segment
    def add_segment(self, position):
        t_object=Turtle(shape='circle')
        t_object.color('white')
        t_object.penup()
        t_object.goto(position)
        self.segments.append(t_object)

    #extending the snake segment
    def extend(self):
        self.add_segment(self.segments[-1].position())
        # new_t.color('white')


    #creating a snake move method
    def move(self):
        #jul16 change the direction of the snake
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        #snake moving forward to set itself
        self.segments[0].forward(STEP_LENGTH)

    #move up
    def up(self):
        if self.segments[0].heading() != HEADING_DOWN:
            self.segments[0].setheading(HEADING_UP)

    #move down
    def down(self):
        if self.segments[0].heading() != HEADING_UP:
            self.segments[0].setheading(HEADING_DOWN)

    #move left
    def left(self):
        if self.segments[0].heading() != HEADING_RIGHT:
            self.segments[0].setheading(HEADING_LEFT)

    #move right
    def right(self):
        if self.segments[0].heading() != HEADING_LEFT:
            self.segments[0].setheading(HEADING_RIGHT)