
##import turtle as t
import sys

##p = t.Pen()
##p.reset()
##p.speed(9000)

def generate_function(A, angle):
	S=""
	while A != "":
		C=A[0:1]
		if (C=="-"):
			S=S+"\n\t\t" + "p.left(" + str(180-angle) + ")"
		elif (C=="+"):
			S=S+"\n\t\t" + "p.right(" + str(angle) + ")"
		elif (C=="A"):
			S=S+"\n\t\t" + "a(distance/2)"
		elif (C=="B"):
			S=S+"\n\t\t" + "b(distance/2)"
		elif (C=="F"):
			S=S+"\n\t\t" + "p.forward(distance)"
		A=A[1:]
	print S


def generate_header(function_name):
	print "def %s(distance):"%function_name
	print "\tif (distance >= 5):"


if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" angle"
        sys.exit(1)

A="-BFA+A+AFB-"
B="+AFB-B-BFA+"

print "##%s"%A
print "##%s"%B
print "import turtle as t"
print "import sys"
print "p = t.Pen()"
print "##p.reset()"
print "p.speed(9999)"

angle = int(sys.argv[1])
generate_header("a")
generate_function(A, angle)
generate_header("b")
generate_function(B, angle)

print "if len(sys.argv) != 2:"
print "\tprint \"Usage: \"+sys.argv[0]+\" length (recommended 75 or less)\""
print "\tsys.exit(1)"
print "length = int(sys.argv[1])"

print "##p.penup()"
print "##p.setx(50-length*3)"
print "##p.sety(50-length*3)"
print "##p.pendown()"
print "a(length)"
print "raw = raw_input()"
