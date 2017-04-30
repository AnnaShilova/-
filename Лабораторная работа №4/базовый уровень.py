str = input('Введите строку: ')
print('замена №1: ',str.replace('!', ' '))

#второй вариант решения

s = input('Введите строку: ')
i = 0
s2 = ''
while i < len(s):
	if s[i] != '!':
		s2 += s[i]
	elif s[i] == '!':
		s2 += ' '
	i += 1
print('замена №2: ',s2)
   
