
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
fred.speed(99999)
R1 = 200
R2 = 100
cycle=1
total_steps=360
steps=360/16

i=0
while i <= 10000:
    t = math.radians(i)
    x = R1*math.cos(t)
    y = R1*math.sin(t)
    t1 = t/8
    x1 = R2*math.cos(t1)
    y1 = R2*math.sin(t1)
    fred.goto(x,y)
    fred.goto(x1,y1)
    i = i+steps

wn.exitonclick()
##a = raw_input()
