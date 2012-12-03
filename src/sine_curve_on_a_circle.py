
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
fred.speed(99999)
XMUL = 10
YMUL = 10
XMUL1 = 100
YMUL1 = 100
cycle=1
total_steps=360
steps=5
i=0
R2const = 100

i=0
while i <= 10000:
    x = XMUL*math.radians(i)
    y = YMUL*math.sin(x)
    t1 = x/16
    R2 = R2const + y
    x1 = R2*math.cos(t1)
    y1 = R2*math.sin(t1)
##    fred.penup()
    fred.goto(x1,y1)
##    fred.pendown()
    i = i+steps

wn.exitonclick()
##a = raw_input()
