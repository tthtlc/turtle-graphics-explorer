
import math
import sys
import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)
end_of_world=1

def hypocycloid(a, b, nos_cycle):
    n=36
    angle=2*PI/n
    fred.penup()
    status=9999
    for i in range(nos_cycle*n):
	   beta = i * angle 
	   x = (a-b)*math.cos(beta) + b*math.cos((a-b)*beta/b)
	   y = (a-b)*math.sin(beta) - b*math.sin((a-b)*beta/b)
           fred.goto(x,y)
	   if (status==9999):
		fred.pendown()
		status=1

if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
	hypocycloid(a, b, 200)
        end_of_world=99

while end_of_world<99:
	a=random.randint(1,400)
	b=random.randint(1,400)
	print a, b
	hypocycloid(a, b, 200)
	raw = raw_input()
	fred.reset()
	fred.clear()
