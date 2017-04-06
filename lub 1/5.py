from math import sin, cos, sqrt, fabs
x = float(input("x = "))
b = 8.1
t = 2
y = x**2 + fabs(x)**(1/3)
a = sqrt(b+t**2)
x = (cos(b))**2 + (sin(a))**2
print ("y = ",y)
print ("a = ",a)
print ("x = ",x)

