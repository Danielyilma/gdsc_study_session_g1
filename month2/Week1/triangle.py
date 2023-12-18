from shape import Shape

class rightTringle(Shape):

    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self,height = height
    
    def area(self):
        return (self.base * self.height)/2