from math import*
MX=[-3.3, 0.4, 4.0, 6.4, 7.6]
MY=[-1.9449,0.3097,2.0913,1.4673,0.6797]
x=-0.8;N=5;Y=0
for k in range(0,N):
    P=1
    for i in range(0,N):
        if not i==k:
            P=P*(x-MX[i])/(MX[k]-MX[i])
    Y=Y+P*MY[k]
Yl=2.1*sin(x*0.31)
poh=(0.024*(x-MX[0])*(x-MX[1])*(x-MX[2])*(x-MX[3])*(x-MX[4]))/120
print (Y,Yl,poh)
