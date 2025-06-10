class Vehicle:
    def start(self):
        pass

class Bike:
    def start(self):
        return "Bike started"

class Car:
    def start(self):
        return "Car started"

vehicles = [Bike(), Car()]

for v in vehicles:
    print(v.start())