
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

def epicycloid(R, r, nos_cycle):
    n=36
    angle=2*PI/n
    a=R
    b=R
    fred.penup()
    flag=9999
    shift=0

    for i in range(nos_cycle):
       for j in range(n):
	   beta = j * angle
	   #x = (a+b)*math.cos(beta) - b*math.cos((a+b)*beta/b)
	   #y = (a+b)*math.sin(beta) - b*math.sin((a+b)*beta/b)
	   x = (a+b)*math.cos(beta) - b*math.cos((a+b)*beta/b)
	   y = (a+b)*math.sin(beta) - b*math.sin((a+b)*beta/b)
	   r = math.sqrt(x*x + y*y)
	   theta = math.atan2(y,x)
	   theta += shift
	   x = r*math.cos(theta)
	   y = r*math.sin(theta)
           fred.goto(x,y)
	   if (flag==9999):
		fred.pendown()
		flag=1
       shift+=angle
       flag=9999
       fred.penup()

epicycloid(100, 10, 36)

wn.exitonclick()
