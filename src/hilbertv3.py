
import turtle as t
import sys

p = t.Pen()
##p.reset()
p.speed(9000)
global magnifier
global distance
global visible_range

magnifier = 1
distance=999
visible_range=20

### A ==== - B F + A F A + F B -
### X=     -YF+XFX+FY-
def a(order):
	global distance
	global visible_range
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
	global visible_range
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
        print "Usage: "+sys.argv[0]+" order (recommended 75 or less)"
        sys.exit(1)

order = int(sys.argv[1])
#distance = int(sys.argv[1])
##magnifier=int(100/length)
##print magnifier
distance=int(100/order)

p.penup()
p.setx(-distance*(2**order))
p.sety(-distance*(2**order))
#p.sety(-distance*2)
p.pendown()
a(order)
raw_input()

