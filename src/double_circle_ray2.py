
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

PI=3.14
angle=2*PI/72

fred = turtle.Turtle()
fred.speed(99999)
R1 = 200
R2 = 100
cycle=1
total_steps=360
steps=1
alpha=2*PI/8

i=0
while i <= 10000:
    t = math.radians(i)
    x = R1*math.cos(3*t)
    y = R1*math.sin(3*t)
    x1 = 100+R2*math.cos(7*t+alpha)
    y1 = 100+R2*math.sin(7*t+alpha)
    fred.penup()
    fred.goto(x,y)
    fred.pendown()
    fred.goto(x1,y1)
    fred.penup()
    i = i+steps

wn.exitonclick()
##a = raw_input()
