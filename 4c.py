#iloczyn skalarny wektorow
import math

class Wektor:
    def __init__(self, x , y , z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __mul__(self, w):
        return self.x * w.x + self.y * w.y + self.z * w.z + self.t *w.t

x = Wektor(1, 2, 12, 4)
y = Wektor(2, 4, 2, 8)

wynik = (x * y)
print("Iloczyn skalarny wynosi: ", wynik)

input("Jesteś świetnym matematykiem!")