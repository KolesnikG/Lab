__author__ = 'KolesnikG'
from math import *
a=0;b=1;h=0.1
x=a;xn=x;yn=0.1;y=yn;
while x<=b:
    print (round(x,3),round(yn,3))
    xn=x
    k1=h*(e**xn+sin(yn))
    k2=h*(e**(xn+h/2)+sin(yn+k1/2))
    k3=h*(e**(xn+h/2)+sin(yn+k2/2))
    k4=h*(e**(xn+h)+sin(yn+k3))
    yn=yn+(k1+2*k2+2*k3+k4)/6
    x+=h
