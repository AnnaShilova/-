i = 1
sum = 0
while i < 1000:
    s = str(i)+' '
    if s[0] == s[1] and s[1] == s[2]:
        sum += 1
    i += 1
print('Количество чисел: ',sum)
    
