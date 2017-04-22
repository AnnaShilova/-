from math import sin, pi
x = int(input('x = '))
n = int(input('n = '))
sum = 0
for i in range(1, n+1):
    sum += (sin(i*(pi/3))*x**i)/i
print('Сумма:', sum)
