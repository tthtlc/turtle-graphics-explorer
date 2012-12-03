
import turtle as t
p = t.Pen()
p.reset()
p.speed(9000)
##p.down()

def triangle(distance):
	if (distance >= 8):
		triangle(distance/2)
		p.forward(distance) 
		p.right(120) 
		triangle(distance/2)
		p.forward(distance) 
		p.right(120) 
		triangle(distance/2)
		p.forward(distance) 
		p.right(120) 

triangle(512)

a = raw_input()
