
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

ngon=10
range_count=20

def star(n, distance):
	angle=360/n/2
	angle=180-angle
	for j in range(range_count):
		p.forward(distance) 
		p.right(angle) 
		p.penup()
		p.forward(40)
		p.pendown()

star(ngon,300)

a = raw_input()


