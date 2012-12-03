
import turtle as t
import math


p = t.Pen()
p.reset()
p.penup()
##p.down()
p.speed(99999)
l=0
j=0
k=0
total_side=360
PI=3.142
step=2*PI/total_side
distance=30
ts = t.getscreen()
ts.colormode(255)

angle=0

for j in range(total_side+1): 
	x=distance*math.sin(2*angle)
	y=distance*math.cos(angle)
	p.goto(x,y)
	if (j==0):
		p.pendown()
	angle+=step
a = raw_input()


