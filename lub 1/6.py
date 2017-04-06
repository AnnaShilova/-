from math import pi, sqrt
R = int(input("радиус нижнего основания = "))
r = int(input("радиус верхнего основания = "))
h = int(input("высота = "))
S1 = pi*R**2
S2 = pi*r**2
V = (h*(S1 + sqrt(S1*S2) + S2))/3
print ("V = ",V)




