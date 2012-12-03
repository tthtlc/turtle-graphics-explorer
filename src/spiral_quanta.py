
import turtle as t
p = t.Pen()
p.reset()
p.down()
i=0
p.speed(22)
for i in range(1000): 
	p.forward(15+i) 
	p.left(i)
	i=i+1
a = raw_input()


