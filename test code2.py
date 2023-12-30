import random
import time


# Обычное слияние двух списков с последующей сортировкой
def merge0(list1, list2):
    lst = list1 + list2
    lst.sort()
    return lst


#  Относительно хорошее слияние – за линейное время (честно украл на форуме у кого-то)
def merge1(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


#  Слияние с одним циклом, без добирания "хвостика" оставшегося списка
#  По факту хуже, чем предыдущий вариант, хотя немного красивее и короче
def merge2(list1, list2):
    i1, i2 = 0, 0
    l1, l2 = len(list1), len(list2)
    rez = list()
    while i1 < l1 or i2 < l2:
        if i1 < l1 and (i2 == l2 or list1[i1] < list2[i2]):
            rez.append(list1[i1])
            i1 += 1
        else:
            rez.append(list2[i2])
            i2 += 1
    return rez


#  Слияние с использованием барьерного элемента
def merge3(list1, list2):
    # Вычисляем элемент, который заведомо больше любого числа в списках
    barrier = max(list1[-1], list2[-1]) + 1
    # Длины списков до изменения запоминаем
    l1, l2 = len(list1), len(list2)
    # Добавляем барьерный элемент в конец обоих списков
    list1.append(barrier)
    list2.append(barrier)
    i1, i2 = 0, 0
    # Результирующий список
    rez = list()
    # Вместо цикла с условием, как в предыдущем варианте, потребуется цикл по диапазону
    for _ in range(l1 + l2):
        # Всего одно сравнение для определения того, элемент из какого списка присоединять к результирующему
        # По идее, такое упрощение условия должно давать выигрыш по скорости,
        if list1[i1] < list2[i2]:
            # Добавляем элемент из первого списка
            rez.append(list1[i1])
            i1 += 1
        else:
            # Добавляем элемент из второго списка
            rez.append(list2[i2])
            i2 += 1
    #  Удаляем барьерный элемент из списков (если они в дальнейшем требуются)
    list1.pop()
    list2.pop()
    return rez


#  Генерируем списки чисел заданного размера
N = 10000000
numbers1 = [random.randint(-1000, 1000) for _ in range(N)]
numbers1.sort()
numbers2 = [random.randint(-1000, 1000) for _ in range(N)]
numbers2.sort()

tm = time.time()
#  Сливаем и выводим послений элемент результирующего списка
#  Печать элемента - привычка из C++, который мог соптимизировать вызов и вообще ничего не делать
print(merge0(numbers1, numbers2)[-1])
print(time.time() - tm, 'секунд – слияние "в лоб" с последующей сортировкой за O(N*logN)')
tm = time.time()
# вызываем функцию
print(merge1(numbers1, numbers2)[-1])
print(time.time() - tm, 'секунд – аккуратный алгоритм слияния за O(N)')
tm = time.time()
# вызываем функцию
print(merge2(numbers1, numbers2)[-1])
print(time.time() - tm, 'секунд – вторая версия алгоритма для слияния за O(N)')
tm = time.time()
# вызываем функцию
print(merge3(numbers1, numbers2)[-1])
print(time.time() - tm, 'секунд – слияние с барьерным элементов за O(N))')
