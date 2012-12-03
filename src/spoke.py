
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
total_side=24
angle=360/total_side
distance=400
ts = t.getscreen()
ts.colormode(255)
#p.setx(-100)
#p.sety(-100)
##p.forward(distance) 
for i in range(total_side+1): 
	p.forward(distance) 
	a=180-angle
	p.left(a)
a = raw_input()


