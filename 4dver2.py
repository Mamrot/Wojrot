#suma macierzy o wymiarach 128x128 wygenerowanych losowo
import random

n = int(input("Podaj wymiar macierzy: "))

x = [[0 for i in range(n)] for j in range(n)]
y = [[0 for i in range(n)] for j in range(n)]
z = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        s = random.randint(-99, 99)
        t = random.randint(-99, 99)
        x[i][j] = s
        y[i][j] = t
        z[i][j] = x[i][j] + y[i][j]

print("Macierz A:")
for i in range(n):
    print(" ".join(map(str, x[i])))

print("Macierz B:")
for i in range(n):
    print(" ".join(map(str, y[i])))

print("Macierz C:")
for i in range(n):
    print(" ".join(map(str, z[i])))