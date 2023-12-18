'''rectangle class module'''
from shape import Shape


class Rectangle(Shape):
    '''class implementation'''

    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

R1 = Rectangle(3, 6)
print(f"{R1.area()= } {R1.perimeter()= }")