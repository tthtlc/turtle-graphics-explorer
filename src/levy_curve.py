
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)
p.penup()
p.sety(100)
p.pendown()

def levy(distance, order):
	if (order > 1):
		p.right(45)
		levy(distance/2, order-1) 
		p.left(90)
		levy(distance/2, order-1) 
		p.right(45)
	else:
		p.forward(distance)

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" order"
        sys.exit(1)

order = int(sys.argv[1])
distance = 8 * (2**order)

levy(distance, order)
raw = raw_input()
