
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
fred.speed(99999)
R1 = 200
R2 = 100
steps=5

i=0
while i <= 10000:
    t = math.radians(i)
    x = R1*math.cos(3*t)
    y = R1*math.sin(3*t)
    x1 = 100+R2*math.cos(4*t)
    y1 = R2*math.sin(4*t)
    fred.penup()
    fred.goto(x,y)
    fred.pendown()
    fred.goto(x1,y1)
    fred.penup()
    i = i+steps

wn.exitonclick()
##a = raw_input()
