#importing modules
from turtle import Turtle
import random

#creating food class
class Food(Turtle):

    #food constructor
    def __init__(self):
        #inheriting turtle constructor characteristics
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        # print('inside food class')
        self.refresh()

    #creating a refresh class for food
    def refresh (self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)