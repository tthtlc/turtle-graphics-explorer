
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
PI=3.14

fred = turtle.Turtle()
fred.speed(99999)
steps=30
w_inner=3
w_outer=90
R_inner=200
R_outer=50
y1=0
x1=0

i=0
while i <= 10000:
    if (y1>=0):
	y1=-R_outer
    else: 
	y1=R_outer
    x1 = x1 + steps
    print y1
    fred.goto(x1,y1)
    i = i+steps

wn.exitonclick()
