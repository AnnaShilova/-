# задание некорректное, поэтому я посчитаю сумму элементов столбцов, а не их количество
import random
n = 3
m = 7
s = 0
matrix = [[random.randint(-10, 10) for j in range(m)] for i in range(n)] 
for row in matrix:                                                   
    print(' '.join([str(elem).rjust(4) for elem in row]))
for j in range(m):
    for i in range(n):
        s += matrix[i][j] # заменить строку на "s += 1", и будет как в задании
    print('Сумма элементов',j+1,'столбца:',s)
    s = 0
