class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def square(self):
            print(self.width * self.height)

    def perim(self):
            print((self.height + self.width) * 2)


small = Rectangle('5','1')
small.square()
small.perim()

big = Rectangle('10','20')
big.square()
big.perim()

middle = Rectangle ('7', '8')
middle.square()
middle.perim()

class Math:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtration(self):
        print(self.a - self.b)

schet = Math('15', '20')

schet.addition()
schet.multiplication()
schet.division()
schet.subtration()

