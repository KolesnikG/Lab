__author__ = 'KolesnikG'
n=110;x=0.1
m=16;t=0.05
a=1;l=(a*t/x)**2
#Создания масива m на n
U=[0]*n
for i in range(n):
    U[i]=[0]*m
#Начальные условия
for j in range(0,2):
    for i in range(1,n-1):
        if i<2:
            U[i][j]=20*x*i
        else:
            U[i][j]=-(20*(x*i-1))/9
#Заполнение масива
for j in range(2,m):
    for i in range(1,n-1):
        U[i][j]=2*(1-l)*U[i][j-1]+l*(U[i+1][j-1]+U[i-1][j-1])-U[i][j-2]
#Вывод массива
for j in range(0,m):
    for i in range(0,n):
        print (round(U[i][j],3), end='\t')
    print (' ')
