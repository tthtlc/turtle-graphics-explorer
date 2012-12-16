
### A ==== - B F + A F A + F B -
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)
ts = t.getscreen()
ts.colormode(255)

def leaf(distance):
	if (distance > 2):
		p.forward(distance)
		p.left(30)
		leaf(distance*2/3) 
		p.forward(distance/2)
		p.left(30)
		leaf(distance*2/3) 
		p.right(60)
		leaf(distance*2/3) 
		p.forward(-distance/2)
		p.left(30)
		p.forward(-distance)
        	j = (distance)%256
        	k = (distance*2)%256
        	l = (distance*3)%256
        	p.pencolor((j,k,l))

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" length"
        sys.exit(1)

length = int(sys.argv[1])
p.setx(-length)
leaf(length)
raw = raw_input()
