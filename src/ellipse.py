
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

PI=3.14
fred = turtle.Turtle()
fred.speed(99999)
fred.penup()
steps=2*PI/360
R1=100
R2=50
i=0
angle=0
alpha=2*PI/8
beta=2*PI/8
while i < 360:
    y1 = R1*math.sin(angle+alpha)####+R1*math.sin(angle+beta)
    x1 = R2*math.cos(angle)####+R2*math.cos(angle)
    fred.goto(x1,y1)
    if (i==0):
	fred.pendown()
    angle += steps
    i+=1

wn.exitonclick()
