'''cicle class module'''
from shape import Shape


class Circle:
    '''circle class implementation'''

    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)