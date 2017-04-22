k = int(input('k = '))
sum = 0
p = 1
for j in range(1,k+1):
  if j != 3 and j != 6 and j != 0:
      p *= (j*(j-6))/(j-3)
      i = j
      for i in range(1, 13):
        if i != 11 and i != 0:
            sum += p * (i+5)**(1/3)/(i-11)
print('Сумма = ', sum)
