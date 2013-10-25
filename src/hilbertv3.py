
import turtle as t
import sys

p = t.Pen()
##p.reset()
p.speed(9000)
global distance

distance=999

### A ==== - B F + A F A + F B -
### X=     -YF+XFX+FY-
def a(order):
	global distance
	if (order >= 1):
		p.left(90) 
		b(order-1)
		p.forward(distance) 
		p.right(90) 
		a(order-1)
		p.forward(distance) 
		a(order-1)
		p.right(90) 
		p.forward(distance) 
		b(order-1)
		p.left(90) 

### B ==== + A F - B F B - F A +
### Y     =+XF-YFY-FX+
def b(order):
	global distance
	if (order >= 1):
		p.right(90) 
		a(order-1)
		p.forward(distance) 
		p.left(90) 
		b(order-1)
		p.forward(distance) 
		b(order-1)
		p.left(90) 
		p.forward(distance) 
		a(order-1)
		p.right(90) 

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" order"
        sys.exit(1)

order = int(sys.argv[1])
distance=int(100/order)

p.penup()
p.setx(-distance*(2**order))
p.sety(-distance*(2**order))
p.pendown()
a(order)
raw_input()

