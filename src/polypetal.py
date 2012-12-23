
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

z_angle=2*PI/15

def polyhedron(R, r, N, n):
    step=2*PI/N
    step1=step/n
    alpha=0
    beta=0
    status=9999
    fred.penup()
    for i in range(n*N):
           x = ((R)*math.cos(beta) + r)*math.cos(alpha)
           y = ((R)*math.cos(beta) + r)*math.sin(alpha)
           beta+=step
           alpha+=step1
           if (status==9999):
		fred.pendown()
		fred.goto(x,y)
		status=1
           fred.goto(x,y)

fred.penup()
polyhedron(100, 50, 36, 20)

wn.exitonclick()
