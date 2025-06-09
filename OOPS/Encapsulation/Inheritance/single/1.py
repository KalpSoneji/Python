class Parent:

    def fnc(self):
        print("Parent fnc called")

class Child(Parent): # passes Parent class as an object to child class

    def fnc2(self):
        print("Child fnc called")
        # self.fnc()

c = Child() # child class default constructor

c.fnc() #parent fnc called through child class
c.fnc2()
