
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)

def star(angle, range_count, distance):
	for j in range(range_count):
		p.forward(distance) 
		p.right(angle) 

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" ngon"
        sys.exit(1)

n = int(sys.argv[1])
#range_count = int(sys.argv[2])
#distance = int(sys.argv[3])
range_count=100
distance=300

### for n=3,5,7,9....the effects are amazing.

angle=360/2/n
angle=180-angle
for i in range(range_count):
	star(angle,n, distance)
	p.right(5)

a = raw_input()
