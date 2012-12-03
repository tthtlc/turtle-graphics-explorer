
import turtle as t
p = t.Pen()
p.reset()
##p.down()

def polygon(n, distance):
	angle=360/n
	for j in range(n): 
		p.forward(distance) 
		p.right(angle) 

total_turn=10 
angle=360/total_turn
for i in range(total_turn): 
	polygon(6,100)
	p.right(angle) 

a = raw_input()
