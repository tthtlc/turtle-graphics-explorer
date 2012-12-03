
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
for i in range(1000): 
	p.circle(50, 270)
	p.up()
	p.circle(50, 90)
	p.forward(8) 
	p.left(4) 
	p.pencolor((0.2,0.8,0.55))
	j = (i+2)%256
	k = (j+2)%256
	l = (k+2)%256
	p.pencolor((j/256,k/256,l/256))
	p.down()
