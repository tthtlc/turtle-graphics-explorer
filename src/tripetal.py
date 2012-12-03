
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

PI=3.14
fred = turtle.Turtle()
fred.speed(99999)
steps=2*PI/360
R1=100
R2=50
i=0
angle=0
alpha=2*PI/8
beta=2*PI/8
while i < 360:
    R2 = R1*math.sin(3*angle+alpha)+1
    x1 = R2*math.cos(angle)
    y1 = R2*math.sin(angle)
    fred.goto(x1,y1)
    angle += steps
    i+=1

wn.exitonclick()
