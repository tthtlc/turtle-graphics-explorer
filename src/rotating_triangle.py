
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(3)
xstep=2
w_inner=3
w_outer=90
R_inner=200
R_outer=10
y1=0
x1=0
xnext=0

omega=2*PI/720
tstep=10
i=0
t=0
while i <= 10000:
    if (i%4==0):
	y1=-R_outer
	ynext=-R_outer
    elif (i%4==2):
	y1=R_outer
	ynext=R_outer
    else:
	xnext=x1 + xstep
	x1=x1+xstep
    x2 = (R_inner+y1)*math.cos(omega*t+x1)
    y2 = (R_inner+y1)*math.sin(omega*t+x1)

    fred.goto(x2,y2)
    ###fred.goto(x1,y1)
    y1=ynext
    x1=xnext
    i=i+1
    t=t+tstep

wn.exitonclick()
