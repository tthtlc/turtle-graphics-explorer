
import math
import turtle as t

p = t.Pen()
p.reset()
p.speed(9999)
PI = 3.14

def celtic(lobe_nos, total_nos,  radius, omega, xx, yy):
	angle=2*PI / total_nos
	theta = 0
	b = lobe_nos
	for j in range(total_nos+1):
		x = radius * (math.cos(b * theta + omega) +1) * math.cos(theta + omega) + xx
		y = radius * (math.cos(b * theta + omega) +1) * math.sin(theta + omega) + yy
		t.goto(x,y)
		t.pendown()
		theta += angle

omega = 0
ngon=32
angle1=2*PI /ngon
Radius = 300
for j in range(ngon):
	t.penup()
	xx = Radius * math.cos(omega)
	yy = Radius * math.sin(omega)
	t.goto(xx,yy)
	celtic(3, 144, 25, omega, xx, yy)
	omega += angle1

a = raw_input()
