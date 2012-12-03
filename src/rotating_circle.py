
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
number_circle=10
angle=360/total_side
small_angle=360/number_circle
for count in range(number_circle):
	p.left(small_angle)
	circle(total_side, distance, angle)
a = raw_input()


