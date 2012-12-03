
### A ==== - B F + A F A + F B -
import turtle as t
import sys
import random

p = t.Pen()
p.reset()
p.speed(9999)
j=0
k=0
l=0
j = random.randint(1,255)
k = random.randint(1,255)
l = random.randint(1,255)
big_angle=60
left_angle=20
right_angle=(big_angle/2)+((big_angle/2)-left_angle)

def tree(distance, j, k, l):
	if (distance > 2):
		k=(k+10)%256
		j=(j+10)%256
		l=(l+10)%256
		p.pencolor((j,k,l))
		p.forward(distance)
		p.left(left_angle)
		tree(distance*4/5, j, k, l) 
		p.right(big_angle)
		tree(distance*2/3, j, k, l) 
		p.left(right_angle)
		p.forward(-distance)

if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" length"
        sys.exit(1)

ts = t.getscreen()
ts.colormode(255)

length = int(sys.argv[1])
p.setx(-length)
tree(length, j, k, l)
raw = raw_input()
