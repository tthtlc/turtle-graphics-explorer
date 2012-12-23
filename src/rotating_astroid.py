
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

def astroid(a, b, nos_cycle):
    n=36
    angle=2*PI/n
    shift=0
    fred.penup()
    flag=9999
    for i in range(nos_cycle/4):
       for j in range(n):
	   beta = j * angle
	   x = (a-b)*math.cos(beta) + b*math.cos((a-b)*beta/b)
	   y = (a-b)*math.sin(beta) - b*math.sin((a-b)*beta/b)
	   r = math.sqrt(x*x + y*y)
	   theta = math.atan2(y,x)
	   theta += shift
	   x = r*math.cos(theta)
	   y = r*math.sin(theta)
           fred.goto(x,y)
	   if (flag==9999):
		fred.pendown()
       shift+=angle
       flag=9999
       fred.penup()

astroid(200, 50, 36)

wn.exitonclick()
