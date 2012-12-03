
import turtle as t

p = t.Pen()
p.reset()
p.down()

def circle(total_side, distance, angle):
	for w in range(total_side):
		p.forward(distance) 
		p.left(angle) 
total_side=24
distance=30
angle=360/total_side
circle(total_side, distance, angle)
a = raw_input()


