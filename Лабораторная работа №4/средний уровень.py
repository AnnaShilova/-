s = str(input('введите строку: '))
s2 = s.split(' ')
for i in range(len(s2)):
    print(s2[i],'(',len(s),')')
    i += 1
