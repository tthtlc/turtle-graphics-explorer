
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)
steps=1
w_inner=2*PI/720/2
w_outer=w_inner*5
w_outer1=w_outer*20
R_inner=100
R_outer=50
R_outer1=10
p=turtle.Pen()

i=0
while i <= 10000:
    slow_angle = (w_inner*i)
    fast_angle = (w_outer*i)
    faster_angle = (w_outer1*i)
    y3 = R_outer1*math.sin(faster_angle)
    x3 = R_outer1*math.cos(faster_angle)
    y2 = (R_outer)*math.sin(fast_angle)
    x2 = (R_outer)*math.cos(fast_angle)
    x1 = (R_inner)*math.cos(slow_angle)
    y1 = (R_inner)*math.sin(slow_angle)
    fred.goto(x1+x2+x3,y1+y2+y3)
    i = i+steps
    if (i%w_outer==0):
    	p.pencolor((i%8/8, (i+7)%8/8, (i+6)%8/8))

wn.exitonclick()
