from random import uniform
mass1 = []
mass2 = []
print('Массив №1')
for i in range(12):
    mass1.append(uniform(-1, 1))
    print(round(mass1[i], 2))
print('Массив №2')
for j in range(12):
    mass2.append(uniform(-1, 1))
    print(round(mass2[j], 2))
print('Новый массив №1')
for i in range(len(mass1)):
    for j in range(len(mass2)):
        if round(mass1[i],2) == round(mass2[j], 2):
            mass1[i] = 0
    print(round(mass1[i], 2))
