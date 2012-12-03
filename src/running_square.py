
import turtle as t
p = t.Pen()
p.reset()
p.speed(9999)
##p.down()

def polygon(n, distance,iter):
	angle=360/n
	real_angle=angle-1
	for j in range(n)*iter: 
		p.forward(distance) 
		p.right(real_angle) 

polygon(4,100,1000)

a = raw_input()
