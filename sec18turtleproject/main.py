#importing modules and classess
from turtle import Turtle, Screen
import random

#workin on objects
chinni = Turtle()
chinni.shape('turtle')
chinni.color('green')
#d#chinni.forward(100)

#d#making a square from turtle
# chinni.forward(100)
# chinni.right(90)
# chinni.forward(100)
# chinni.right(90)
# chinni.forward(100)
# chinni.right(90)
# chinni.forward(100)
# chinni.right(90)

#d#3jl making a dashed line with turtle
# for step in range(15):
#     chinni.forward(10)
#     chinni.penup()
#     chinni.forward(15)
#     chinni.pendown()

#d#3jl drawing shapes of different colors with chinni
# pen_color = ['red', 'blue', 'green', 'orange', 'purple', 'brown','cyan']
# for no_of_sides in range(4,11):
#     angle = 360//no_of_sides
#     for edge in range(no_of_sides):
#         chinni.pencolor(pen_color[no_of_sides-4])
#         chinni.forward(100)
#         chinni.right(angle)

#d#3jl random walk
# movements = [1, 2, 3, 4]
# for step in range(50):
#     step_direction = random.choice(movements)
#     if step_direction == 1:
#         chinni.pensize(10)
#         chinni.speed(10)
#         chinni.pencolor('red')
#         chinni.forward(30)
#     elif step_direction == 2:
#         chinni.pensize(10)
#         chinni.speed(10)
#         chinni.pencolor('green')
#         chinni.backward(30)
#     elif step_direction == 3:
#         chinni.pensize(10)
#         chinni.speed(10)
#         chinni.pencolor('cyan')
#         chinni.right(30)
#     elif step_direction == 4:
#         chinni.pensize(10)
#         chinni.speed(10)
#         chinni.pencolor('brown')
#         chinni.left(30)

#3jl spirograph
# chinni.colormode(255)
for angle in range(0,360,3):
    # r = random.randint(0,255)
    # g = random.randint(0,255)
    # b = random.randint(0,255)
    # chinni.pencolor((r, g, b))
    chinni.speed(30)
    chinni.setheading(angle)
    chinni.circle(100)
    

#last two lines of code
my_screen = Screen()
my_screen.exitonclick()
