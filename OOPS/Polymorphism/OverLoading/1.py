class A:
    def test(self):
        print("No arg") 
    
    def test(self, a):
        print("1 arg : ", a)

a = A()
a.test()

# since python is a scripting lang, it reads line by line and hence polymorphism can't be applied directly
# whichever fnc is last declared is considered by python, and args have to be passed accordingly