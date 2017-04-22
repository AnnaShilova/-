n = str(input("n = "))
i = 0
j = len(n)-1
simm = True
for i in range(j):  
    if n[i] != n[j]:
        simm = False
    i += 1
    j -= 1
if simm:
    print('число симметрично')
else:
    print('число несимметрично')
    
