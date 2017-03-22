q = int (input("первое: "))
w = int (input("второе: "))
e = int (input("третье: "))
if ((q > w) and (q > e)):
    print("больше",q)
elif ((w > q) and (w > e)):
    print("больше", w)
elif ((e > w) and (e > w)):
    print("больше", e)
