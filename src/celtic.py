
import math
import turtle as t

p = t.Pen()
p.reset()
p.speed(9999)
PI = 3.14

def celtic(lobe_nos, total_nos,  radius):
	angle=2*PI / total_nos
	theta = 0
	b = lobe_nos
	for j in range(total_nos*b):
		x = radius * (math.cos(b * theta) +1) * math.cos(theta)
		y = radius * (math.cos(b * theta) +1) * math.sin(theta)
		t.goto(x,y)
		t.pendown()
		theta += angle

t.penup()
celtic(4, 144, 100)

a = raw_input()
