
### A ==== - B F + A F A + F B -
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9000)

def generic_snowflake(ngon, distance, level):
	ngon_exterior_angle = 180 - (360/ngon)
	for i in range(ngon):
		side(distance, level)
		p.right(ngon_exterior_angle)
	
def side(distance, level):
	if (level == 0):
		p.forward(distance) 
	else:
		side(distance/3, level-1)
		p.left(45) 
		side(distance/3, level-1)
		p.right(45) 
		side(distance/3, level-1)
		p.right(45) 
		side(distance/3, level-1)
		p.left(45) 
		side(distance/3, level-1)

if len(sys.argv) != 4:
        print "Usage: "+sys.argv[0]+" ngon distance level"
        sys.exit(1)

ngon = int(sys.argv[1])
length = int(sys.argv[2])
level = int(sys.argv[3])

generic_snowflake(ngon, length, level)
raw = raw_input()
