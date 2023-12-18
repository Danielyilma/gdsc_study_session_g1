'''car module'''

class car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display(self):
        print("Make: ", self.make)
        print("model: ", self.model)
        print("year: ", self.year)
