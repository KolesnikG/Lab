__author__ = 'KolesnikG'
from math import *
a=0;b=1;y0=0.1;h=0.1
x=a;y=y0
while(x<=b):
    print (round(x,3),round(y,3))
    x+=h;y+=h*(e**x+sin(y))
