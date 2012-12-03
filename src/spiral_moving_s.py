
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
ts = t.getscreen()
ts.colormode(255)
start=30
for i in range(2000): 
	p.circle(start+j, 180)
	p.circle(-start-j, 180)
	p.penup()
	p.circle(-start-j, 180)
	p.circle(start+j, 180)
	j=j+i/50
	p.pendown()
	p.left(3) 
