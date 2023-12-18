'''base class shape module'''


class Shape:
    '''shape class implementation'''

    def __init__(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self, color):
        self.__color = color

    def area(self):
        '''to be implemented by sub class'''
        pass
    