a = int (input("a = "))
b = int (input("b =  "))
c = int (input("c = "))
d = int (input("d = "))
z = 0
if (a < b):
    i = a
    while (i < b):
        i += 1
        if (i % d == c):
            print(i, end=' ')
            z += 1
        else:
            if z == 0:
                print("Таких чисел нет")
else:
    print ("Неверно задан диапазон")  
