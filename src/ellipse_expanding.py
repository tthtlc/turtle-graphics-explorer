
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

PI=3.14
fred = turtle.Turtle()
fred.speed(99999)
angle_step=2*PI/180
r1_step = 5
r2_step = -5

def ellipse(R1, R2, alpha, beta):
	i=0
	angle=0
	while i < 180:
	    y1 = R1*math.sin(angle+alpha)####+R1*math.sin(angle+beta)
	    x1 = R2*math.cos(angle)####+R2*math.cos(angle)
	    fred.goto(x1,y1)
	    if (i==0):
	    	fred.pendown()
	    angle += angle_step
	    i+=1
	fred.penup()

fred.penup()
beta=2*PI/8
alpha=2*PI/8
R1=80
R2=40
i=0
while i <= 30:
	ellipse(R1, R2, alpha, beta)
	R1 += r1_step
	R2 += r2_step
	alpha += 2*angle_step
	#beta -= angle_step
	
wn.exitonclick()
