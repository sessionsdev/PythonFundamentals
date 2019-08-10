'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

from math import pi

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self. width = width

    def calc_area(self):
        area = self.length * self.width
        return area

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        area = pi * self.radius**2
        return area

rec = Rectangle(5, 5)
cir = Circle(6)

print(rec.calc_area())
print(cir.calc_area())
