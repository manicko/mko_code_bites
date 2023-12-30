import timeit

'''
    Basic timeit framework to test code snippets by Alex Glozman
    Version:  1.3
    Modified: 27.07.2022
'''
# general test setup
REPETISIONS = 100  #  число повторений

# function to run the test
def run_test(code_setup, code_to_test, comment='', number=REPETISIONS, g_vars={}, measure=None, cnt=[0]):
    cnt[0] += 1  # автоматическая нумерация тестов
    if measure:
        mtype, attempts = measure
        times = timeit.repeat(stmt=code_to_test, setup=code_setup, number=number, globals=g_vars, repeat=attempts)
        if mtype == 'average':
            elapsed_time = sum(times) / len(times)
        elif mtype == 'best':
            elapsed_time = min(times)
        elif mtype == 'worst':
            elapsed_time = max(times)
        print(f'test {cnt[0]}, elapsed_time: {elapsed_time:.6f}, from {number} repeats, measure {measure}, ({comment})')
    else:
        elapsed_time = timeit.timeit(stmt=code_to_test, setup=code_setup, number=number, globals=g_vars)
        print(f'test {cnt[0]}, elapsed_time: {elapsed_time:.6f}, from {number} repeats, ({comment})')


# генерируем рандомальную строку из повторяющихся слов
import random as rnd
from string import ascii_letters
NUM_WORDS = 100_000
WORD_MIN_LEN, WORD_MAX_LEN = 5, 15
MAX_WORD_FREQ = 100

c = 0
lst = []
while c < NUM_WORDS:
    w = ''.join(rnd.sample(ascii_letters, rnd.randint(WORD_MIN_LEN, WORD_MAX_LEN)))
    freq = rnd.randint(1, MAX_WORD_FREQ)
    lst += [w] * freq
    c += freq
rnd.shuffle(lst)
s = ' '.join(lst)

# делаем строку s доступной для среды timeit
local_vars = {'s': s}

empty_setup = '''#пусто'''

code_to_test1 = '''
d = {}
for w in s.split():
    d[w] = d.get(w, 0) + 1
res = min(d, key=lambda x: (-d[x], x))
'''

code_to_test2 = '''
frequency = {}
for w in s.split():
    frequency[w] = frequency.get(w, 0) + 1
res = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))[0][0]
'''

code_to_test3 = '''
from collections import Counter
res = Counter(s.split()).most_common()[1][0]
'''

code_to_test4 = '''
f = {i:s.count(i) for i in set(s.split())}
res = min(s.split(), key=lambda x: (-f[x], x))
'''

code_to_test5 = '''
d = {}
max_val = 0
max_w = ''
for w in s.split():
    if w in d:
        d[w] += 1
        if d[w] >= max_val:            
            max_val = d[w]
            if w < max_w:
                max_w = w
    else:
        d[w] = 1
        
res = max_w
'''

run_test(empty_setup, code_to_test1, g_vars=local_vars, comment='словарь и выбор минимального')
run_test(empty_setup, code_to_test2, g_vars=local_vars, comment='словарь и сортировка результатов')
run_test(empty_setup, code_to_test3, g_vars=local_vars, comment='словарь Counter')
# run_test(empty_setup, code_to_test4, g_vars=local_vars, comment='метод count и выбор минимального')
run_test(empty_setup, code_to_test5, g_vars=local_vars, comment='метод с поиском максимального при создании словаря')