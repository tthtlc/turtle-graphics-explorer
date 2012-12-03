
import turtle as t
p = t.Pen()
p.reset()
p.speed(9000)
##p.down()

def square(distance):
	if (distance >= 4):
		p.forward(distance) 
		square(distance/2)
		p.right(90) 
		p.forward(distance) 
		square(distance/2)
		p.right(90) 
		p.forward(distance) 
		square(distance/2)
		p.right(90) 
		p.forward(distance) 
		square(distance/2)
		p.right(90) 

square(100)

a = raw_input()
