
import turtle as t
p = t.Pen()
p.reset()
##p.down()

def polygon_spoke(n, distance):
	angle=360/n
	for j in range(n): 
		p.forward(distance) 
		p.right(180) 
		p.forward(distance) 
		p.right(180) 
		p.right(angle) 

polygon_spoke(6,100)

a = raw_input()
