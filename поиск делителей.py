n = int(input())
for x in range(1, n+1):
    print(x, end='')
    # заканчиваем поиск на корне из числа, т.к. знаем, что все делители парные
    end = int(x**0.5)
    for i in range(1, end + 1):
        if i**2 == end**2 == x:
            # исключаем дубли если можно извлечь натуральный корень (напр. 2*2 = 4)
            print('+', end='')
        elif x % i == 0:
            # два, т.к. делители парные, напр. для 12: 1 и 12, 2 и 6, 3 и 4.
            print('++', end='')
    print()
