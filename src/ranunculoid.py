
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14
R_outer=50
R_inner=200

fred = turtle.Turtle()
fred.speed(99999)

def epicycloid(a, b, nos_cycle):
    n=360
    angle=2*PI/n
    for i in range(nos_cycle*n):
	   beta = i * angle 
	   x = (a+b)*math.cos(beta) - b*math.cos((a+b)*beta/b)
	   y = (a+b)*math.sin(beta) - b*math.sin((a+b)*beta/b)
           ##x = ((r)*math.cos(beta) + r*beta*math.cos(alpha))
           ##y = direction*(r)*math.sin(beta)+r*beta*math.sin(alpha)
	   ##x = R*math.cos(beta/20)+x
	   ##y = R*math.sin(beta/20)+y
           fred.goto(x,y)

epicycloid(50, 10, 100)

wn.exitonclick()
