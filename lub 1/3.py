from math import sin, log, e
x = float(input("x = "))
y = float(input("y = "))
k = float(input("k = "))
U = (log((x**3)+y)-y**4)/((e**y)+5.4*k**3)
print ("U = ",U)
