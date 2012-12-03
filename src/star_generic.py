
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9999)
##p.down()

#### ngon=5, range_count=5
#### ngon=6, range_count=12
#### ngon=8, range_count=180
#### ngon=10, range_count=20
#### ngon=12, range_count=24

def star(n, range_count, distance):
	angle=360/n/2
	angle=180-angle
	for j in range(range_count):
		p.forward(distance) 
		p.right(angle) 

if len(sys.argv) != 3:
        print "Usage: "+sys.argv[0]+" ngon range_count"
        sys.exit(1)

ngon = int(sys.argv[1])
range_count = int(sys.argv[2])

star(ngon,range_count, 300)

a = raw_input()
