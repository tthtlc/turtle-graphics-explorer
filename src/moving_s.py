
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
	p.circle(50, 180)
	p.circle(-50, 180)
	p.penup()
	p.circle(-50, 180)
	p.circle(50, 180)
	p.pendown()
	p.left(3) 
