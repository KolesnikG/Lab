__author__ = 'KolesnikG'
from math import *
x=0;eps=0.001
d=0.1;G=0

def Function(x):
    return e**(fabs(x-0.2))-4*x

y=Function(x);
while (fabs(d)>eps/4):
    G=y;x+=d
    y=Function(x)
    if y>G:
        d/=-4
print('Xmin=',x,'\nYmin=',y);
