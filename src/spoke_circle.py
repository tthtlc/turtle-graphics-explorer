
import turtle as t
p = t.Pen()
p.reset()
##p.down()
p.speed(300)
l=0
j=0
k=0
total_side=24
angle=360/total_side
distance=40
spoke_distance=10
ts = t.getscreen()
ts.colormode(255)
for j in range(total_side+1): 
	p.up()
	p.forward(spoke_distance) 
	p.down()
	for i in range(total_side+1): 
		p.forward(distance) 
		a=180-angle
		p.left(a)
	p.right(a)
	p.up()
	p.left(180)
	p.forward(spoke_distance) 
	p.left(180)
	p.left(angle)
a = raw_input()


