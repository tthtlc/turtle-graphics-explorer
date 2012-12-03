
import math
import turtle

PI=3.14
angle90=90
steps=1

i=0
while i <= 10000:
    fast_angle = math.radians(angle90*i)
    y = math.sin(fast_angle)
    print y
    i = i+steps

