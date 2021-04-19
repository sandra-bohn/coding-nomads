'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle():
    def __init__(self, length, width, units):
        "defines dimensions of rectangle"
        self.length = length
        self.width = width
        self.units = units
    def __str__(self):
        "describes rectangle"
        return f"{self.length} {self.units} by {self.width} {self.units} rectangle"
    def area(self):
        "calculates area of rectangle"
        return self.length * self.width
    def perimeter(self):
        "calculates perimeter of rectangle"
        return 2 * self.length + 2 * self.width

class Circle():
    def __init__(self, radius, units):
        "defines circle by dimensions"
        self.radius = radius
        self.units = units
    def __str__(self):
        "describes circle"
        return f"{self.radius} {self.units} radius circle"
    def area(self):
        "calculates area of circle"
        return self.radius * self.radius * 3.14
    def circum(self):
        "calculates circumference of circle"
        return self.radius * 2 * 3.14
