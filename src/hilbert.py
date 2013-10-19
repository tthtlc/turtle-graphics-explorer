
### A ==== - B F + A F A + F B -
import turtle as t
import sys

p = t.Pen()
##p.reset()
p.speed(9000)

def a(distance):
	if (distance >= 5):
		p.left(90) 
		b(distance/2)
		p.forward(distance) 
		p.right(90) 
		a(distance/2)
		p.forward(distance) 
		a(distance/2)
		p.right(90) 
		p.forward(distance) 
		b(distance/2)
		p.left(90) 

### B ==== + A F - B F B - F A +
def b(distance):
	if (distance >= 5):
		p.right(90) 
		a(distance/2)
		p.forward(distance) 
		p.left(90) 
		b(distance/2)
		p.forward(distance) 
		b(distance/2)
		p.left(90) 
		p.forward(distance) 
		a(distance/2)
		p.right(90) 

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" length (recommended 75 or less)"
        sys.exit(1)

length = int(sys.argv[1])
p.penup()
p.setx(50-length*3)
p.sety(50-length*3)
p.pendown()
a(length)
raw = raw_input()
