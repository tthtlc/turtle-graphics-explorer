
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)
p.penup()
p.setx(-300)
p.pendown()
angle=60

###X ===> YF+XF+Y
###Y ===> XF−YF−X

def a(distance, order):
	if (order > 1):
		b(distance/2,order-1)
		p.right(angle)
		a(distance/2,order-1)
		p.right(angle)
		b(distance/2,order-1)
	else:
		p.forward(distance)

def b(distance, order):
	if (order > 1):
		a(distance/2,order-1)
		p.left(angle)
		b(distance/2,order-1)
		p.left(angle)
		a(distance/2,order-1)
	else:
		p.forward(distance)


if len(sys.argv) != 3:
        print "Usage: "+sys.argv[0]+" order distance"
        sys.exit(1)

order = int(sys.argv[1])
distance = int(sys.argv[2])

### a good number is order = 7 and distance = 600

a(distance, order)
raw = raw_input()
