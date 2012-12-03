
### A ==== - B F + A F A + F B -
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9000)

def snowflake(distance, level):
	for i in range(3):
		side(distance, level)
		p.right(120)
	
def side(distance, level):
	if (level == 0):
		p.forward(distance) 
	else:
		side(distance/3, level-1)
		p.left(60) 
		side(distance/3, level-1)
		p.right(120) 
		side(distance/3, level-1)
		p.left(60) 
		side(distance/3, level-1)

if len(sys.argv) != 3:
        print "Usage: "+sys.argv[0]+" length level"
        sys.exit(1)

length = int(sys.argv[1])
level = int(sys.argv[2])
snowflake(length, level)
raw = raw_input()
