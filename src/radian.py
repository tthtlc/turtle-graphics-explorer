
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)
steps=1
w_inner=3
w_outer=90
R_inner=200
R_outer=50

i=0
while i <= 360:
    angle = math.radians(i)
    x2 = R_outer*math.cos(angle)
    y2 = R_outer*math.sin(angle)
    print(angle)
    print(x2)
    print(y2)


wn.exitonclick()
