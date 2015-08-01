__author__ = 'KolesnikG'
from math import *
a=0;b=1;h=0.1
x=a;y=0;k=0.001;y1=h;i=0;yk=0.1
def F(x,y):
    return (e**x+sin(y))
while x<b:
    print(round(x,3),round(yk,3),i)
    yk=0;i=0
    y+=h*F(x,y)
    while (fabs(yk-y1))>k:
        yk=y1
        y1=y+h/2*(F(x,y)+F(x+h,yk))
        i+=1
    x+=h;
