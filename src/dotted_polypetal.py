
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

def polyhedron(R, r, N, n, k):
    step=2*PI/N
    step1=step/n
    alpha=0
    beta=0
    xprev=9999
    yprev=9999
    fred.penup()
    for i in range(n*N):
           x = ((R)*math.cos(beta) + r)*math.cos(alpha)
           y = ((R)*math.cos(beta) + r)*math.sin(alpha)
           beta+=step
           alpha+=step1
           if (xprev==9999):
		fred.pendown()
		fred.goto(x,y)
		status=1
           	xprev=x
           	yprev=y
	   else:
		gx = x - xprev
		gy = y - yprev
		x1 = k*gx+x
		y1 = k*gy+y
           	fred.goto(x1,y1)
		fred.pendown()
           	fred.goto(x,y)
		fred.penup()
		xprev=x
		yprev=y

fred.penup()
polyhedron(100, 50, 36, 20, 0.2)

wn.exitonclick()
