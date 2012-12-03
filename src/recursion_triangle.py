
import turtle as t
p = t.Pen()
p.reset()
##p.down()

def triangle(distance):
	if (distance >= 4):
		p.forward(distance) 
		p.right(120) 
		triangle(distance/2)
		p.forward(distance) 
		p.right(120) 
		triangle(distance/2)
		p.forward(distance) 
		p.right(120) 
		triangle(distance/2)

triangle(100)

a = raw_input()
