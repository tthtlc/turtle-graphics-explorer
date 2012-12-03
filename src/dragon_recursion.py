
### Heighway's Dragon
import turtle as t
import sys

global toggle
p = t.Pen()
p.reset()
p.speed(9999)
p.penup()
p.sety(-100)
p.setx(-100)
p.pendown()


##p.forward(1200)

def dragon(distance, order, toggle):
	if (order > 1):
		p.right(45*toggle*-1)
		dragon(distance/2, order-1, toggle) 
		p.left(90*toggle*-1)
		dragon(distance/2, order-1, toggle) 
		p.right(45*toggle*-1)
	else:
		p.forward(distance)

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" order"
        sys.exit(1)

order = int(sys.argv[1])
distance = 10 * (2**order)

dragon(distance, order, 1)
raw = raw_input()
