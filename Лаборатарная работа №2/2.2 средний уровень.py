from math import fabs
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
sr = (a+b+c)/3
print("Числа, которые больше среднего: ")
if (fabs(a) > sr) or (fabs(b) > sr) or (fabs(c) > sr):
    print(a, b, c)
elif (fabs(a) > sr) and (fabs(b) > sr) or (fabs(c) > sr):
    print(a, b)
elif (fabs(a) > sr) or (fabs(b) > sr) and (fabs(c) > sr):
    print(c)
else:
    print("таких чисел нет")
