
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
fred.speed(99999)
steps=1
w_inner=1
w_outer=20
R_inner=200
R_outer=50

i=0
while i <= 10000:
    slow_angle = w_inner*math.radians(i)
    fast_angle = w_outer*math.radians(i)
    x1 = R_inner*math.cos(slow_angle)
    y1 = R_inner*math.sin(slow_angle)
    x2 = R_outer*math.cos(fast_angle)
    y2 = R_outer*math.sin(fast_angle)
    fred.goto(x1+x2,y1+y2)
    i = i+steps

wn.exitonclick()
