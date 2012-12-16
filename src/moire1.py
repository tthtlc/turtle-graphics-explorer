
import turtle as t
import random

p = t.Pen()
p.up()
p.reset()
p.speed(22)
l=0
j=0
k=0
ts = t.getscreen()
ts.colormode(255)

def moire(max_radius, total_nos_ring, x, y):
	p.setx(x)
	p.sety(y)
	p.down()
	step=max_radius/total_nos_ring
	for i in range(max_radius): 
		p.circle(i*step)
		p.up()
		p.right(90)
		p.forward(step)
		p.left(90)
	###	p.pencolor((0.2,0.8,0.55))
		l = (i+random.randint(1,255))%256
		k = (l+10)%256
		m = (k+10)%256
		p.pencolor((j,k,l))
		p.down()
	p.up()


moire(100, 20, -100, 0)
moire(100, 20, 100, 0)
a=raw_input()
