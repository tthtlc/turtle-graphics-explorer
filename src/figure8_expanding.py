
import turtle as t
import math


p = t.Pen()
p.reset()
p.penup()
p.speed(99999)
total_side=360
PI=3.142
step=2*PI/total_side
ts = t.getscreen()
ts.colormode(255)


def figure8(distance, tilt_angle):
	angle=0
	for j in range(total_side): 
		x=distance*math.sin(2*(angle+tilt_angle))
		y=distance*math.cos(angle+tilt_angle)
		p.goto(x,y)
		if (j==0):
			p.pendown()
		angle+=step
	p.penup()


distance=30
tilt_angle=30*step

for i in range(40): 
	figure8(distance, tilt_angle)
	distance+=5
	tilt_angle+=5*step

a = raw_input()


