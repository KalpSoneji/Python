#make a parameterized constructor of parent class and use it in child class

class Boss:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self, name, id):
        print(f"Name: {name}, ID: {id}")

class Employee(Boss):

    def __init__(self):
        super().__init__("Kalp", 10)

    def success(self):
        print("Success")

e = Employee()
e.details("Kalp", 10)
e.success()