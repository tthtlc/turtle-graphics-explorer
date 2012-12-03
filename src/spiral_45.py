
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
angle=360/8
ts = t.getscreen()
ts.colormode(255)
for i in range(1000): 
	p.forward(i*4) 
	a=180/angle
	p.left(180-a)
	j = (j+2)%256
	k = (k+2)%256
	l = (l+2)%256
	p.pencolor((j,k,l))
	p.pencolor("blue")
a = raw_input()


