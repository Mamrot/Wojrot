import random

a = [ ]
for i in range(10):
   a.append(random.randint(0,30))

print(a)

from random import randrange


def sortowanie(lista):
    if len(lista) < 2:
        return lista
    pivot = len(lista)//2
    i = 0
    j = len(lista)-1
    print(j)
    while(i<j):
        while (lista[i] < lista[pivot]):
            i += 1
        while (lista[j] > lista[pivot]):
            j -= 1
        p = lista[i]
        lista[i] = lista[j]
        lista[j] = p
    print(1)
    return(sortowanie(lista[:pivot+1]),sortowanie(lista[pivot+1:]))

print(sortowanie(a))