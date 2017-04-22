from math import cos
x = 0.1
print(' x  |   y ')
while x <= 3:
    y = (1+x)**(1/2)-3*cos(x)
    print(round(x,2),'|', round(y,2))
    x += 0.2
