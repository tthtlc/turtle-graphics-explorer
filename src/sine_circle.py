
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
radius = 100

for angle in range(360):
    y = radius * math.sin(math.radians(angle))
    x = radius * math.cos(math.radians(angle))
   ### print(x,y)
    fred.goto(x,y)

wn.exitonclick()
a = raw_input()
