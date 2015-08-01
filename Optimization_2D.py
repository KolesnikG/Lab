__author__ = 'KolesnikG'
from math import *
x=[0,0];eps=0.001;
n=2;A=0;B=1

def function(*x):
    return 2.2*x[0]-1.3*x[1]+exp(0.04*x[0]**2+0.12*x[1]**2)

def optimization(i,*x):
    d=0.1;G=0;x=list(x);
    T=function(x[0],x[1]);
    while (fabs(d)>eps/4):
        G=T;x[i]+=d
        T=function(x[0],x[1]);
        if T>G:d/=-4
    return x[i]

while(fabs(A-B))>eps:
    A=function(x[0],x[1]);
    for i in range(0,n):
        x[i]=optimization(i,x[0],x[1])
    B=function(x[0],x[1])
print('x1=',x[0],'\nx2=',x[1])
