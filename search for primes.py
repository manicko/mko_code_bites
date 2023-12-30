prime_number = 10001

a = 2
b = 10000000


# задаем нечетную нижнюю границу поиска (a = 8, граница - 9 и т.д., но больше 3)
start = max(a + 1 - a % 2, 3)
# сюда будем сохранять проверенные значения, исключая все степени этого числа (3, 9, 27 и тд)
primes = [2]
checked = set()
checked.add(2)
for n in range(start, b + 1, 2):  # смотрим среди нечетных, до верхней границы включительно
    if not n**0.5 in checked:
        flag = True
        # проверка на натуральность, с 3 т.к. четные мы исключили
        for i in range(3, int(n**0.5) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            primes.append(n)
            if len(primes) >= prime_number:
                print(primes[-1])
                break
    # заносим число в словарь, чтобы исключить его степени в будущем
    checked.add(n)
