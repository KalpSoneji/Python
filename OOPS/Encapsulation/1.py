class Demo:

    x = 100 #class level variable

    def test(self):
        
        a = 1000 #local level variable

        print("Test fnc...")

        print(f"Value of x = ", {self.x}) # ways of accessing variable (since we're accessing global variable) 
        print(f"Value of x = ", {Demo.x}) # ways of accessing variable (since we're accessing global variable)
        print("Value of a = ",a) #it can be accessed directly as it is a local variable

        self.name = "Royal";

def myTest(self):
    print("Value of name = ", self.name) # we could access name due to self being common

d = Demo() #object creation
d.test() #calling function

print("Value of x = ", d.x) # accessing variable through object

# d.myTest()

print(d.name)
