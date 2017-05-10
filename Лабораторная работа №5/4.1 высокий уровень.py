from random import randrange
mass = []
for i in range(5):
    mass.append(randrange(1, 10))
    print(bin(mass[i]))
print('_________')
for i in range(5):
    mass[i] += 10
    print(bin(mass[i]))
