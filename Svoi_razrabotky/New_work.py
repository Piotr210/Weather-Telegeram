a=input('Введите строку с повторяющимися элементами: ')
b=a
for i in b:
    if a.count(i)>1:
        a=a.replace(i,'')
print(b)
print(a)

