from abc import ABC, abstractmethod

class Vehicle:

    @abstractmethod
    def start(self):
        pass

    def end(self):
        print("Ending")

class Car(Vehicle):

    def start(self):
        print("Starting")

BMW = Car()
BMW.start()
BMW.end()

# if we make an abstract method and keep it empty, it throws error
# any number of abstract and non-abstract methods can be made
# non-abstract methods don't need to be re-written in child class