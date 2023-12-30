# input example: '3 7'
n, m = map(int, input().split())
print()

matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()


#n, m = map(int, input().split())
print()

matrix = [[j * n + i + 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()

print()

matrix = [[(i + 1) * m - j
           for j in range(m)]
          for i in range(n)]

for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()

print()

#n, m = map(int, input().split())

matrix = [[i * m + j + 1 if i % 2 == 0
           else (i + 1) * m - j
           for j in range(m)]
          for i in range(n)]

for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()

print()

matrix = [[i % n + j % m + 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()

print()

#n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
counter = 0
for i in range(m+n-1):
    for j in range(max(0, i-m+1), min(i+1, n)):
        counter += 1
        matrix[j][i-j] = counter


for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()


print()

l = [[0] * m for _ in range(n)]
k = 1
for j in range(m + n):
    for i in range(n):
        if 0 <= j - i < m:
            l[i][j - i] = k
            k += 1
for i in range(n):
    print(*l[i])


print()


#n, m = map(int, input().split())


matrix = [[0 for _ in range(m)] for _ in range(n)]


counter = 1

i = 0
j = 0
x = 0
step = 1

while counter <= m*n:
    while m - 1 - x > j >= x and counter <= m*n:
        matrix[i][j] = counter
        counter += 1
        j += step

    while n - 1 - x > i >= x and counter <= m*n:
        matrix[i][j] = counter
        counter += 1
        i += step

    while m - 1 - x >= j > x and counter <= m*n:
        matrix[i][j] = counter
        counter += 1
        j -= step

    while n - 1 - x >= i > x and counter <= m*n:
        matrix[i][j] = counter
        counter += 1
        i -= step

    x += 1
    j += step
    i += step
    if counter == m*n:
        matrix[i][j] = counter
        counter += 1


for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:<3}', end='')
    print()

print()
#n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
dr, dc, r, c = 0, 1, 0, 0

for cnt in range(1, n * m + 1):
    a[r][c] = cnt

    if a[(r + dr) % n][(c + dc) % m]:
        dr, dc = dc, -dr

    r += dr
    c += dc

for row in a:
    print(*(f'{e:<3}' for e in row), sep='')
