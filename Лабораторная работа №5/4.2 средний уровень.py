import random
n = int(input('Введите длину стороны квадратной матрицы: '))
s = 0
print('Вводите матрицу',n,'на',n)
matrix = [[input() for j in range(n)] for i in range(n)] 
for row in matrix:                                                   
    print(' '.join([str(elem) for elem in row]))
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
                s = 1
if s == 0:
    print('Матрица симметрична относительно главное диагонали')
else:
    print('Матрица не симметрична относительно главной диагонали')

