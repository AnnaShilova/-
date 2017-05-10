from random import uniform
from math import fabs
mass = []
prP = 1
prO = 1
for i in range(15):
    mass.append(uniform(-10, 10))
    print(round(mass[i], 2))
    if mass[i] > 0:
        prP *= mass[i]
    else:
        prO *= mass[i]
raz = prP - fabs(prO)
print('разность = ',round(raz, 2))
