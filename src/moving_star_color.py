
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

l=0
j=0
k=0
ts = t.getscreen()
ts.colormode(255)

angle=360/2/n
angle=180-angle
for i in range(range_count):
	star(angle,n, distance)
	p.right(5)
###     p.pencolor((0.2,0.8,0.55))
        j = (j+13)%256
        k = (k+11)%256
        l = (l+7)%256
        p.pencolor((j,k,l))

a = raw_input()
