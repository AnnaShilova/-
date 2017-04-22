n = str(input('n = '))
m = {}
for i in n:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
for i in sorted(m):
    print('Число',i,'встречается',m[i],'раз')
