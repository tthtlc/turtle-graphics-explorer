
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

def polyhedron(Rx, Ry, Rz, n):
    step=2*PI/n
    alpha=0
    beta=0
    for i in range(n):
       for j in range(n):
           x = ((R_outer)*math.cos(beta) + R_inner)*math.cos(alpha)
           z = ((R_outer)*math.cos(beta) + R_inner)*math.sin(alpha)
           y = (R_outer)*math.sin(beta)
           xp=x-z*math.cos(z_angle)
           yp=y-z*math.sin(z_angle)
           beta+=step
           fred.goto(xp,yp)
           if (j==0):
		fred.pendown()
		xbegin=xp
		ybegin=yp
       fred.goto(xbegin,ybegin)
       fred.penup()
       alpha+=step

fred.penup()
polyhedron(200, 200, 200, 32)

wn.exitonclick()
