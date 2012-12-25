
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)

#### d==r means epicycloid

def epitrochoid(R, r, d, nos_cycle):
    n=72
    angle=2*PI/n
    fred.penup()
    status=9999
    for i in range(nos_cycle*n):
	   beta = i * angle 
	   x = (R+r)*math.cos(beta) - d*math.cos((R+r)*beta/r)
	   y = (R+r)*math.sin(beta) - d*math.sin((R+r)*beta/r)
           fred.goto(x,y)
	   if (status==9999):
		fred.pendown()
		status=1


epitrochoid(40, 50, 20, 5)

wn.exitonclick()
