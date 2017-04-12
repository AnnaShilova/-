slovo = str(input('Слово: '))
q = slovo[::-1]
if slovo == q:
    print("слово является палиндром")
else:
    print("слово не является палиндром")
