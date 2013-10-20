##-BBAA+FF+AABB-
##+AABB-FF-BBAA+
import turtle as t
import sys
p = t.Pen()
##p.reset()
p.speed(9999)
def a(distance):
	if (distance >= 5):

		p.left(135)
		b(distance/2)
		b(distance/4)
		a(distance/2)
		a(distance/2)
		p.right(45)
		p.forward(distance)
		p.forward(distance)
		p.right(45)
		a(distance/2)
		a(distance/2)
		b(distance/4)
		b(distance/2)
		p.left(135)
def b(distance):
	if (distance >= 5):

		p.right(45)
		a(distance/2)
		a(distance/4)
		b(distance/2)
		b(distance/2)
		p.left(135)
		p.forward(distance)
		p.forward(distance)
		p.left(135)
		b(distance/2)
		b(distance/2)
		a(distance/4)
		a(distance/2)
		p.right(45)
if len(sys.argv) != 2:
	print "Usage: "+sys.argv[0]+" length (recommended 75 or less)"
	sys.exit(1)
length = int(sys.argv[1])
##p.penup()
##p.setx(50-length*3)
##p####.sety(50-length*3)
##p.pendown()
a(length)
raw = raw_input()
