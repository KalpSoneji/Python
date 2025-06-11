class Circle:

    pi = 3.14 # Class variable, in order to access it, write className.variable

    @staticmethod # how to define a static method
    def area(r):
        return Circle.pi * pow(r, 2)
    
print(Circle.area(10))