# Multiple parent, single child

class Boss:
    def __init__(self):
        print("Boss called")

    def btask(self):
        print("Bring me signing papers")

class Manager:  
    def __init__(self):
        print("Manager called")

    def mtask(self):
        print("Bring me coffee")

class Employee(Boss, Manager): # since boss is passed as a parameter first, 'Employee' inherits 'Boss' methods/properties
    def __init__(self):
        super().__init__()

    def work(self):
        self.btask()
        self.mtask()

emp1 = Employee()
emp1.work()