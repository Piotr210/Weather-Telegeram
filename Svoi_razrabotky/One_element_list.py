try:
    arrlist = list(
        map(int, input('Введите значения элементов списка через запятую, он полностью целочисленный: ').split(',')))
    for i in range(10000000):
        if arrlist.count(i) > 1:
            while i in arrlist:
                arrlist.remove(i)
    print(arrlist)
except ValueError:
    print('Вы вели не тот тип данных, нужно вводить целые числа')

