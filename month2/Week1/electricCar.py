

class ElectricCar(car):

    def __init__(Self, make, model, year, battery_capacity):
        car.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        car.display_info(self)
        print(f"Battery Capacity: {self.battery_capacity} kWh")

    def charge_battery(self):
        print("Charging the battery...")