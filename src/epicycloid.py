
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

def epicycloid(a, b, nos_cycle):
    n=72
    angle=2*PI/n
    fred.penup()
    status=9999
    for i in range(nos_cycle*n):
	   beta = i * angle 
	   x = (a+b)*math.cos(beta) - b*math.cos((a+b)*beta/b)
	   y = (a+b)*math.sin(beta) - b*math.sin((a+b)*beta/b)
           fred.goto(x,y)
	   if (status==9999):
		fred.pendown()
		status=1

epicycloid(50, 10, 1)

wn.exitonclick()
