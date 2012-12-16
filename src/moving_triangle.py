
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
n=3
ts = t.getscreen()
ts.colormode(255)
angle=360/n

def polygon(distance,angle,n):
	for i in range(n): 
		p.forward(distance)	
		p.left(angle)

for i in range(1000): 
	polygon(50, angle, n)
	p.left(5)
	p.forward(i/10) 
###	p.pencolor((0.2,0.8,0.55))
	j = (j+2)%256
	k = (k+2)%256
	l = (l+2)%256
	p.pencolor((j,k,l))
a = raw_input()


