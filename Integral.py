from math import *
# Метод трапеций
a=1;b=2;n=5000;s=0;x=a;h=(b-a)/n
for i in range(1,n-1):
    x+=h;s+=x**2
print((s+((a**2)+(b**2))/2)*h)
# Метод Симпсона
h=(b-a)/(n-1);xc=a-h;s=0;xnc=0
while xnc<b:
    s=s+2*(xnc**2);
    xc+=2*h;s+=4*(xc**2);xnc=xc+h
print(h/3*(s+a**2+b**2))
