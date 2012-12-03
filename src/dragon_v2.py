
#### x->X+YF+ y=>-fx-y
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)
angle=90

def x(order):
	if (order > 1):
		x(order-1)
		p.right(angle)
		y(order-1)
		p.right(angle)
	else:
		p.forward(distance)

def y(order):
	if (order > 1):
		p.left(angle)
		x(order-1)
		p.left(angle)
		y(order-1)
	else:
		p.forward(distance)


if len(sys.argv) != 3:
        print "Usage: "+sys.argv[0]+" order distance"
        sys.exit(1)

order = int(sys.argv[1])
distance = int(sys.argv[2])

#### good example of input:   order = 10 and distance = 10
x(order)
raw = raw_input()
