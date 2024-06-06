import random

m=[]
det=1
print("Ввод данных\n")
choose=int(input("Введите 1, чтобы матрица \nзаполнилась случайными числами: "))
n=int(input("\nЗадание порядка матрицы: "))

if choose==1: 
    for i in range(n):
        m.append(random.sample(range(1,10),n))
else:
    for i in range(n):
        m.append([])
        print("Ввод значений в ",i+1,"строку матрицы: ")
        for i2 in range(n):
            m[i].append(0)
            m[i][i2]=int(input(": "))

print('\nИсходная матрица:') 
for i in range(n):
    print(m[i])

for i in range(n-1): 
    for i1 in range(n-1-i):
        k=m[i1+1+i][i]/m[i][i]
        for i2 in range(n-i):
            m[i1+1+i][i2+i]-=m[i][i2+i]*k

for i in range(n):
    det*=m[i][i]

print('\n\nРезультат:') 
print("det A = ",round(det))

\begin{verbatim}
import random
m=[]
det=1
print("Ввод данных\n")
choose=int(input("Введите 1, чтобы матрица \nзаполнилась случайными числами: "))
n=int(input("\nЗадание порядка матрицы: "))

if choose==1: 
    for i in range(n):
        m.append(random.sample(range(1,10),n))
else:
    for i in range(n):
        m.append([])
        print("Ввод значений в ",i+1,"строку матрицы: ")
        for i2 in range(n):
            m[i].append(0)
            m[i][i2]=int(input(": "))

print('\nИсходная матрица:') 
for i in range(n):
    print(m[i])

for i in range(n-1): 
    for i1 in range(n-1-i):
        k=m[i1+1+i][i]/m[i][i]
        for i2 in range(n-i):
            m[i1+1+i][i2+i]-=m[i][i2+i]*k

for i in range(n):
    det*=m[i][i]

print('\n\nРезультат:') 
print("det A = ",round(det))
\end{document}
