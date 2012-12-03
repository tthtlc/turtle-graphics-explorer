
import turtle as t
p = t.Pen()
p.reset()
p.speed(9000)
##p.down()

def odd_shape(distance, orientation):
	if (distance >= 100):
		odd_shape(distance/2, orientation*-1)
		p.right(90) 
		p.forward(distance) 
		odd_shape(distance/2, orientation*-1)
		p.right(90*orientation) 
		p.forward(distance) 
		odd_shape(distance/2, orientation*-1)
		p.right(90*orientation) 
		p.forward(distance) 
		odd_shape(distance/2, orientation*-1)

odd_shape(100, 1)

a = raw_input()
