
### A ==== - B F + A F A + F B -
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)

def tree(distance):
	if (distance > 2):
		p.forward(distance)
		p.left(30)
		tree(distance*2/3) 
		p.right(60)
		tree(distance*2/3) 
		p.left(30)
		p.forward(-distance)

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" length"
        sys.exit(1)

length = int(sys.argv[1])
p.setx(-length)
tree(length)
raw = raw_input()
