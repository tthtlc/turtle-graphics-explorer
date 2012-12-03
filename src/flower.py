
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)
steps=2
w_inner=1
w_outer=10
R_inner=100
R_outer=100
p=turtle.Pen()

i=0
while i <= 10000:
    slow_angle = math.radians(w_inner*i)
    fast_angle = math.radians(w_outer*i)
    y2 = R_outer*math.sin(fast_angle)
    x1 = (R_inner+y2)*math.cos(slow_angle)
    y1 = (R_inner+y2)*math.sin(slow_angle)
    fred.goto(x1,y1)
    i = i+steps
    if (i%w_outer==0):
    	p.pencolor((i%8/8, (i+7)%8/8, (i+6)%8/8))

wn.exitonclick()
