
import turtle as t
p = t.Pen()
p.reset()
p.speed(9999)
##p.down()

def polygon_spoke_star(n, distance):
	angle=360/n
	for j in range(n): 
		p.forward(distance) 
		poly_star(5,50)
		p.right(180) 
		p.forward(distance) 
		p.right(180) 
		p.right(angle) 

def poly_star(n, distance):
	angle1=360/n/2
	angle1=180-angle1
	for j in range(n): 
		p.forward(distance) 
		p.right(angle1) 

polygon_spoke_star(6,100)

a = raw_input()
