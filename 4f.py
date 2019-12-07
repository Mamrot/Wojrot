#Obliczanie wyznacznika macierzy wygenerowanej losowo
import random
import numpy as np

n = int(input("Podaj wymiar macierzy: "))

x = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        s = random.randint(-5, 5)
        x[i][j] = s

wynik=np.linalg.det(x)


print("Macierz A:")
for i in range(n):
    print(" ".join(map(str, x[i])))

print("Wyznacznik macierzy wynosi: ", wynik)
