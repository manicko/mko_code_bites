import time
import random


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        stop = True
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                stop = False
        if stop is True:
            break
    return a


def selection_sort(a):
    n = len(a)
    k = 1
    while k < n:
        m_j = n - k
        for j in range(n - k):
            if a[j] > a[m_j]:
                m_j = j
        a[n - k], a[m_j] = a[m_j], a[n - k]
        k += 1

    return a


def insertion_sort(a):
    if (n := len(a)) <= 1:
        return
    for i in range(1, n):
        key = a[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == '__main__':
    size = 10

    lst = list(range(size))
    random.shuffle(lst)
    to_sort = lst[:]
    print(to_sort)

    REPETITIONS = 1000

    bg0 = time.time()
    for _ in range(REPETITIONS):
        res0 = bubble_sort(to_sort)
    end0 = time.time()
    print(f'{end0 - bg0:.6f}', ' bubble_sort')
    # print(res0)

    to_sort = lst[:]
    print(to_sort)
    bg1 = time.time()
    for _ in range(REPETITIONS):
        res1 = selection_sort(to_sort)
    end1 = time.time()
    # print(res1)
    print(f'{end1 - bg1:.6f}', ' selection_sort')

    to_sort = lst[:]

    print(to_sort)
    bg2 = time.time()
    res2 = 0
    for _ in range(REPETITIONS):
        res2 = insertion_sort(to_sort)
    end2 = time.time()
    print(res2 == sorted(to_sort))
    print(f'{end2 - bg2:.6f}', ' insertion_sort')

    # print(res0 == res1 and res0 == res2)
