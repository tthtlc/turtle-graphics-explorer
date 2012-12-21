
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
alpha=2*PI/8
beta=2*PI/8

def sine_curve(n):
	i=0
	angle=0
	while i < 360:
	    y1 = R1*math.sin(angle)####+R1*math.sin(angle+beta)
	    x1 = R2*math.cos(n*angle)####+R2*math.cos(angle)
	    fred.goto(x1,y1)
	    if (i==0):
		fred.pendown()
	    angle += steps
	    i+=1
	
fred.penup()
fred.setx(-100)
fred.sety(0)
sine_curve(2)


fred.penup()
fred.setx(0)
fred.sety(0)
sine_curve(3)

fred.penup()
fred.setx(0)
fred.sety(0)
sine_curve(4)

fred.penup()
fred.setx(0)
fred.sety(0)
sine_curve(5)

fred.forward(10)

wn.exitonclick()
