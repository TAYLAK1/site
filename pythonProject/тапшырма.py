class Shape:
    def __init__(self,abc):
        self.abc = abc
    def perimetr(self):
        pass
class Circle:
    def __init__(self, dc):
        self.dc = dc
    def perimetr(self):
        return f'{self.dc * 2 * 3.14} sm'
circle1 = Circle(2)
print(circle1.perimetr())  # ... sm

class Rectangle:
    def __init__(self,po, pi):
        self.po = po
        self.pi = pi
    def perimetr(self):
        return f'{(self.po + self.pi) * 2} sm'
rec1 = Rectangle(2, 3)
print(rec1.perimetr())  # 28 sm

class Triangle(Rectangle):
    def __init__(self,po, pi, lo):
        super().__init__(po, pi)
        self.lo = lo
    def perimetr(self):
        return f'{self.po * self.pi * self.lo} sm'
triangle1 = Triangle(5, 6, 2)
print(triangle1.perimetr())  # 60 sm