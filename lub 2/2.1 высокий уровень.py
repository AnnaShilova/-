x = float(input('x = '))
y = float(input('y = '))
if not ((y >= -x) and (y >= x) and (y <= 1)) and ((y <= 2) and (x <= 1) and (x >= -1)):
    print('Точка входит в область')
else:
    print('Точка не входит в область')
