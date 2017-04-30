s = str(input('введите предложение: '))
s2 = s.split(' ')
for i in range(len(s2)):
    j = i-1
    while j >= 0:
        if s2[i] == s2[j]:
            print('Слово, которое повторяется: ',s2[i])
            break
        else:
            j -= 1
        
   
        
    
