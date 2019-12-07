#mnożenie dwoch macierzy o wymiarach 8x8
import random

n = 8#int(input("Podaj wymiar macierzy: "))

x = [[0 for i in range(n)] for j in range(n)]
y = [[0 for i in range(n)] for j in range(n)]
z = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        s = random.randint(0, 9)
        t = random.randint(0, 9)
        x[i][j] = s
        y[i][j] = t

for i in range(n):
    for j in range(n):
        for k in range(n):
            z[i][j] = z[i][j] + x[i][k] * y[k][j]

print("Macierz A:")
for i in range(n):
    print(" ".join(map(str, x[i])))

print("Macierz B:")
for i in range(n):
    print(" ".join(map(str, y[i])))

print("Macierz C:")
for i in range(n):
    print(" ".join(map(str, z[i])))