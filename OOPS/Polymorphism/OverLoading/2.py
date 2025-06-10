class Calc:
    
    def add(self,a=0,b=0,c=0):
        print(f"value of a = {a} b = {b} c = {c}")
        return a + b + c

c = Calc()

print(c.add())
print(c.add(10))
print(c.add(10,90))
print(c.add(10,90,100))

# since default values have been passed while making the function, it doesn't show error