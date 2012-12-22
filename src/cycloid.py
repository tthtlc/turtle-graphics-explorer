
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

def cycloid(r, k, nos_cycle, direction):
    n=36
    angle=2*PI/n
    x=1
    y=0
    for i in range(nos_cycle*n):
	   beta = i * angle 
	   x = r*(beta-math.sin(beta))
	   y = r*(1-math.cos(beta))
	   ### equally valid
           ###x = ((r)*math.cos(beta) + r*beta)
           ###y = direction*(r)*math.sin(beta)
           fred.goto(x,y)

cycloid(10, 0.1, 100, -1)

wn.exitonclick()
