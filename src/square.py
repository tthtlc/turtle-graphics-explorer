
import turtle as t
p = t.Pen()
p.reset()
##p.down()

def polygon(n, distance):
	angle=360/n
	for j in range(n): 
		p.forward(distance) 
		p.right(angle) 

polygon(4,100)

a = raw_input()
