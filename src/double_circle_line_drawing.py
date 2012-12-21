
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

PI=3.14
fred = turtle.Turtle()
fred.speed(9999)
fred.penup()
steps=2*PI/36
R1=300
R2=20
i=0
angle=0
alpha=2*PI/8
beta=2*PI/8
t=0
while t < 360:
	i=0
	angle=0
	while i < 36:
	    y1 = R2*math.sin(angle+alpha)+R1*math.sin(t)####+R1*math.sin(angle+beta)
	    x1 = R2*math.cos(angle)+R1*math.cos(t)####+R2*math.cos(angle)
	    fred.setx(x1-30)
	    fred.sety(y1-30)
	    fred.pendown()
	    fred.goto(x1,y1)
	    fred.penup()
	    angle += steps
	    i+=1
	t+=steps

wn.exitonclick()
