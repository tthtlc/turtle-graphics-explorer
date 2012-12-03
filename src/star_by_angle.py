
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)

def star(angle, range_count, distance):
	for j in range(range_count):
		p.forward(distance) 
		p.right(angle) 

if len(sys.argv) != 4:
        print "Usage: "+sys.argv[0]+" angle range_count distance"
        sys.exit(1)

angle = int(sys.argv[1])
range_count = int(sys.argv[2])
distance = int(sys.argv[3])

star(angle,range_count, distance)

a = raw_input()
