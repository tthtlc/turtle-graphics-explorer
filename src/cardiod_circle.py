
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)

def mycircle(R, cx, cy, start_angle):
    n=120
    angle=2*PI/n
    fred.penup()
    x = cx+R*math.cos(start_angle*2*PI/360) 
    y = cy+R*math.sin(start_angle*2*PI/360) 
    fred.setx(x)
    fred.sety(y)
    fred.pendown()
    for t in range(n+1):
	   beta = t * angle + start_angle*2*PI/360
	   x = cx+R*math.cos(beta) 
	   y = cy+R*math.sin(beta) 
           fred.goto(x,y)
    fred.penup()

def myepicircle(R, cx, cy, start_angle):
    n=36
    angle=2*PI/n
    fred.penup()
    x = cx+R*math.cos(start_angle*2*PI/360) 
    y = cy+R*math.sin(start_angle*2*PI/360) 
    x0=x
    y0=y
    fred.setx(x)
    fred.sety(y)
    fred.pendown()
    for t in range(n+1):
	   beta = t * angle + start_angle*2*PI/360
	   x = cx+R*math.cos(beta) 
	   y = cy+R*math.sin(beta) 
           my_r = math.sqrt((x-x0)**2 + (y-y0)**2)
	   if (x-x0)==0:
	   	epi_start_angle = PI
	   else:
	   	epi_start_angle = PI-math.atan((y-y0)/(x-x0))
	   mycircle(my_r, x, y, epi_start_angle)
    fred.penup()

myepicircle(100, 10, 100, 90)

wn.exitonclick()
