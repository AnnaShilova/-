s = str(input('введите строку: '))
s2 = ''
s3 = ''
for i in range(len(s)):
    if s[i] == 'я':
        s2 += str(' ')
    else:
        s2 += s[i]
for i in range(len(s2)):
    s3 += s2[i-1]
print(s3)
