
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)
steps=1
w_inner=3
w_outer=90
R_inner=200
R_outer=50

i=0
while i <= 10000:
    slow_angle = math.radians(w_inner*i)
    fast_angle = math.radians(w_outer*i)
    x2 = R_outer*math.cos(fast_angle)
    y2 = R_outer*math.sin(fast_angle)
    x1 = (R_inner+y2)*math.cos(slow_angle)
    y1 = (R_inner+y2)*math.sin(slow_angle)
    fred.goto(x1,y1)
    print y2
    i = i+steps

wn.exitonclick()
