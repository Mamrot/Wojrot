#suma macierzy o wymiarach 128x128 wygenerowanych losowo

import random
#import numpy as np


def random_tab(n: int):
    return [[random.randint(-9, 9) for x in range(n)] for y in range(n)]

print(random_tab(3))

def random_tab2(n: int):
    return [[random.randint(-9, 9) for x in range(n)] for y in range(n)]

print(random_tab2(3))


input("Jesteś świetnym matematykiem!")