
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)
steps=5
w_inner=2*PI/360
w_outer=20*2*PI/360
R_inner=200
R_outer=50

i=0
while i <= 10000:
    slow_angle = math.radians(w_inner*i)
    fast_angle = math.radians(w_outer*i)
    x1 = R_inner*math.cos(slow_angle)
    y1 = R_inner*math.sin(slow_angle)
    x2 = R_outer*math.cos(fast_angle)
    y2 = R_outer*math.sin(fast_angle)
    fred.goto(x1+x2,y1+y2)
    i = i+steps

wn.exitonclick()
