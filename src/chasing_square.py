
import turtle as t
import random

p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
ngon=4
ts = t.getscreen()
ts.colormode(255)
angle=360/ngon
angle-=1
j = random.randint(0,255)
k = random.randint(0,255)
l = random.randint(0,255)

for i in range(1000): 
	p.forward(i*3) 
	p.left(angle)
###	p.pencolor((0.2,0.8,0.55))
	p.pencolor((j,k,l))
	j=(j+2)%256
	k=(k+2)%256
	l=(l+2)%256
	if (i%16==0):
		j = random.randint(0,255)
		k = random.randint(0,255)
		l = random.randint(0,255)
	

a = raw_input()


