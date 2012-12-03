
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
total_side=24
angle=360/total_side
distance=100
ts = t.getscreen()
ts.colormode(255)
for w in range(total_side):
	for i in range(total_side): 
		p.forward(distance) 
		a=180-(angle)
		p.left(a)
		j = (j+2)%256
		k = (k+2)%256
		l = (l+2)%256
		p.pencolor((j,k,l))
		p.pencolor("blue")
	p.penup
	distance += 50
	p.forward(distance) 
	p.left(a)
	p.pendown
a = raw_input()


