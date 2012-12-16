
import turtle as t
import sys

p = t.Pen()
p.reset()
p.speed(9000)
##p.down()

def leaf(distance, x, y):
	if (distance > 2):
		p.forward(distance)
		p.left(20)
		p.forward(distance*3/4)
		p.left(20)
		p.forward(distance/2)
		p.left(20)
		p.forward(distance/4)
		p.left(20)

		(x,y) = p.position()
		leaf(distance*2/3, x, y) 

		p.forward(distance)
		p.right(20)
		p.forward(distance*3/4)
		p.right(20)
		p.forward(distance/2)
		p.right(20)
		p.forward(distance/4)
		p.right(20)

		p.penup()
		p.setx(x)
		p.sety(y)
		p.pendown()



if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" length"
        sys.exit(1)

length = int(sys.argv[1])
p.setx(-length)
(x,y) = p.position()
leaf(length, x, y)
raw = raw_input()
