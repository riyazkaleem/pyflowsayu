#oop theory
#each object has two things: attributes(what the object has),  methods(what the object does)
#class is blueprint has objects
#function linked to an object is called a method
#turtle graphics: https://docs.python.org/3/library/turtle.html
#python package is group of collection of modules

#importing modules
import turtle
import auxmodule
import prettytable

#testing by importing variable from another module
print(f'imported from another module: aux4variable: {auxmodule.aux4variable}')

#importing objects from turtle
chinni = turtle.Turtle()
screen4obj = turtle.Screen()

#printing object chinni, accessing attributes of turtle object
print(chinni)
chinni.shape("turtle")
chinni.color("DarkOrchid2")

#printing attribute of screen object
print(f'screen height: {screen4obj.canvheight}')

#moving chinni forward 100 units
chinni.forward(100)

#accessin another method from the screen object
screen4obj.exitonclick()

#6/24/24
#importing class from prettytable
from prettytable import PrettyTable

#creating object from pretty table class
table = PrettyTable()
table.add_column("pokemon name", ["pikachu", "squirtle", "charmander"])
table.add_column("type",["electric","water","fire"])
table.align = 'l'
print(table)



