#Klasa liczb zespolonych
import math

class ComplexNumber():

    Wynik = 0

    def __init__(self, re , im):
        self.a = re
        self.b = im


    def Numb(self):
        print('%s + %si'%(self.a, self.b))

    def Adding(self,y):
        print("Wynik dodawania: "'%s + %si'%(self.a + y.a, self.b + y.b))

    def Subing(self, y):
        print("Wynik odejmowania: "'%s + %si' % (self.a - y.a, self.b - y.b))

    def Multy(self, y):
        print("Wynik mnożenia: "'%s + %si' % ((self.a * y.a-self.b * y.b),(self.b*y.a+self.a*y.b)))

    def __str__(self):
        return "({0},{1})".format(self.a, self.b)

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return ComplexNumber(x, y)

    def __sub__(self, other):
        x = self.a - other.a
        y = self.b - other.b
        return ComplexNumber(x, y)

x = ComplexNumber(1, -3)
y = ComplexNumber(-2, 1)

#x.Numb()
#y.Numb()

#x.Adding(y)
#x.Subing(y)
#x.Multy(y)
print(x+y)

n = str(input("Wybierz działanie(+/-/*): "))
#Wynik = 0

if n == '+':
    print(x+y)
elif n == '-':
    print(x-y)
elif n =='*':
    x.Multy(y)
