
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)

z_angle=2*PI/15

def polyhedron(Rx, Ry, Rz, n):
    step=2*PI/n
    alpha=0
    beta=0
    for i in range(n):
       for j in range(n):
           x = (Rx)*math.cos(alpha)*math.cos(beta)
           y = (Rz)*math.sin(alpha)
           z = (Rz)*math.cos(alpha)*math.sin(beta)
           xp=x-z*math.cos(z_angle)
           yp=y-z*math.sin(z_angle)
           alpha+=step
           fred.goto(xp,yp)
           if (j==0):
		fred.pendown()
		xbegin=xp
		ybegin=yp
       fred.goto(xbegin,ybegin)
       fred.penup()
       beta+=step

fred.penup()
polyhedron(200, 200, 200, 32)

wn.exitonclick()
