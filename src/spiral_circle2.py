
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
ts = t.getscreen()
ts.colormode(255)
for i in range(2000): 
	p.circle(50, 270)
	p.up()
	p.circle(50, 90)
	p.forward(10) 
	p.left(6) 
	if (i%4)==0:
		p.forward(10)
		p.right(10)
###	p.pencolor((0.2,0.8,0.55))
	j = (j+2)%256
	k = (k+2)%256
	l = (l+2)%256
	p.pencolor((j,k,l))
	p.down()
