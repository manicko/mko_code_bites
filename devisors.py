# объявление функции
def get_factors(n):
    low_devisors = []
    high_devisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # делители низшего порядка по возрастанию
            low_devisors.append(i)
            if n // i != i:
                # делители высшего порядка по убыванию
                high_devisors.append(n // i)

        # инвертируем чтобы высший порядок шел по возрастанию
    return len(low_devisors + high_devisors[::-1])


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))

# упорядоченные devisors без сортировки
from collections import deque
def get_factors_fast(n):
    nsqrt = n ** .5
    factors = deque()
    if nsqrt.is_integer():
        factors.append(int(nsqrt))
    for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
        if n % i == 0:
            factors.appendleft(i)
            factors.append(n // i)
    return list(factors)

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {n: get_factors_fast(n) for n in numbers}