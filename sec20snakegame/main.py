#import modules
from turtle import Turtle, Screen

#creating objects
screenu = Screen()

#linking the attributes to the objects
screenu.bgcolor('green')
screenu.setup(height=600, width=600)

#creating a snake
x_positions=[0, -20, -40]
all_objects = []
# print(chinni.position())
# print(chinni.turtlesize())
for t_index in range(3):
    t_object=Turtle(shape='circle')
    t_object.color('white')
    t_object.penup()
    t_object.goto(x=x_positions[t_index], y=0)
    all_objects.append(t_object)

#trying to move the snake
game_is_on = True
while game_is_on:
    for obj in all_objects:
        obj.forward(20)

#final screen method for exit on click
screenu.exitonclick()