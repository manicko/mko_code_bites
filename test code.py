import time


def swithMinMax1(s: str):
    nums = list(map(int, s.split()))

    idx_min = min(range(len(nums)), key=lambda i: nums[i])
    idx_max = max(range(len(nums)), key=lambda i: nums[i])
    nums[idx_min], nums[idx_max] = nums[idx_max], nums[idx_min]

    res = ' '.join(map(str, nums))
    return res


def swithMinMax2(s: str):
    a = list(map(int, s.split()))
    x = a.index(max(a))
    y = a.index(min(a))
    a[x], a[y] = a[y], a[x]
    res = ' '.join(map(str, a))
    return res


REPETITIONS = 10000
s = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 180 19 20 21 22'

bg0 = time.time()
for _ in range(REPETITIONS):
    res = swithMinMax1(s)
end0 = time.time()
print(f'{end0 - bg0:.6f}', ' swithMinMax1')

bg1 = time.time()
for _ in range(REPETITIONS):
    res = swithMinMax2(s)
end1 = time.time()
print(f'{end1 - bg1:.6f}', ' swithMinMax2')
