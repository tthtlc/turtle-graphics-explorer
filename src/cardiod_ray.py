
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
    n=120
    angle=2*PI/n
    displaced_angle1=2*PI/3
    displaced_angle2=2*PI/4
    a=R
    b=R
    for i in range(nos_cycle*n):
	   beta = i * angle 
	   x = (a+b)*math.cos(beta) - b*math.cos((a+b)*beta/b)
	   y = (a+b)*math.sin(beta) - b*math.sin((a+b)*beta/b)
	   x1 = (a+b)*math.cos(beta+displaced_angle1) - b*math.cos((a+b)*(beta+displaced_angle1)/b)
	   y1 = (a+b)*math.sin(beta+displaced_angle1) - b*math.sin((a+b)*(beta+displaced_angle1)/b)
	   x2 = (a+b)*math.cos(beta+displaced_angle2) - b*math.cos((a+b)*(beta+displaced_angle2)/b)
	   y2 = (a+b)*math.sin(beta+displaced_angle2) - b*math.sin((a+b)*(beta+displaced_angle2)/b)
	   fred.penup()
	   fred.setx(x)
	   fred.sety(y)
           fred.pendown()
           fred.goto(x1,y1)
           fred.goto(x2,y2)
	   fred.penup()
           ##x = ((r)*math.cos(beta) + r*beta*math.cos(alpha))
           ##y = direction*(r)*math.sin(beta)+r*beta*math.sin(alpha)
	   ##x = R*math.cos(beta/20)+x
	   ##y = R*math.sin(beta/20)+y
           fred.goto(x,y)

epicycloid(100, 10, 100)

wn.exitonclick()
