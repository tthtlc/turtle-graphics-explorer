
import turtle as t
p = t.Pen()
p.reset()
p.speed(9999)
##p.down()

#### ngon=5, range_count=5
#### ngon=6, range_count=12
#### ngon=8, range_count=180
#### ngon=10, range_count=20
#### ngon=12, range_count=24

ngon=5
range_count=5

def star_ngon(n, distance):
	angle=360/n/2
	angle=180-angle
	for j in range(range_count):
		p.forward(distance) 
		p.right(angle) 
	angle=360/n
	p.right(angle) 
	distance=distance*0.6203

	for j in range(range_count):
		p.forward(distance) 
		p.left(angle) 
	p.left(angle) 


nangle=360/ngon
for j in range(range_count):
	p.forward(50) 
	star_ngon(ngon,300)
	p.forward(-50) 
	p.left(nangle) 

a = raw_input()
