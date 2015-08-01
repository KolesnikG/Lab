from math import*
MX=[1.10,1.15,1.25,1.30,1.35]
MY=[0.89121,0.91276,0.94898,0.96356,0.97572]
x=1.2; N=5
# Создание двумерного списка
MK=[0]*N
for i in range(N):
    MK[i]=[0]*N
# Оперделение формулы Ньютона
if ((MX[0]-MX[4])/2)<x:
    Method=True
    q=(x-MX[0])/(MX[1]-MX[0])
else:
    Method=False
    q=(x-MX[4])/(MX[1]-MX[0])
# Нахождение конечных разниц
i=1;temp=1
for j in range(0,N-1):
    MK[i][j]=MY[j+1]-MY[j]
for i in range(2,N):
    temp+=1
    for j in range(0,N-temp):
        MK[i][j]=MK[i-1][j+1]-MK[i-1][j]
# Нахождение значения полинома в точке х
for i in range(0,N):
    temp=1
    if Method==True:
        P=MY[0]
        for i in range(1,N):
            P+=MK[i][0]*q/temp
            q*=q-i; temp*=i+1
    else:
        P=MY[N-1]
        for i in range(1,N):
               P+=MK[i][N-i-1]*q/temp
               q*=q+i; temp*=i+1
# Результат
print (P)
