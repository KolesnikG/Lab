__author__ = 'KolesnikG'
from math import *
x=[0,0];A=0;B=1
eps=0.001;h=0.1

def function(*x):
    return 2.2*x[0]-1.3*x[1]+exp(0.04*x[0]**2+0.12*x[1]**2)

def gradF(i,*x):
    x=list(x)
    f1=function(x[0],x[1])
    x[i]+=eps
    f2=function(x[0],x[1])
    return (f2-f1)/eps

while fabs(A-B)>eps:
    A=function(x[0],x[1]);
    for i in range(0,2):
        x[i]-=h*gradF(i,x[0],x[1])
    B=function(x[0],x[1])
print('x1=',x[0],'\nx2=',x[1])
