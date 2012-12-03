
### A ==== - B F + A F A + F B -
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9000)

def right_left(distance, level):
	if (level > 1):
		p.right(45) 
		right_left(distance/2, level-1)
	else:  ### (level == 1):
		p.forward(distance) 
	if (level > 1):
		p.left(90) 
		right_left(distance/2, level-1)
	else: ### (level == 1):
		p.forward(distance) 
	if (level > 1):
		p.right(45) 

if len(sys.argv) != 3:
        print "Usage: "+sys.argv[0]+" level distance"
        sys.exit(1)

level = int(sys.argv[1])
distance = int(sys.argv[2])
right_left(distance, level)
raw = raw_input()
