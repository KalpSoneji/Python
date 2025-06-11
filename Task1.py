class Money:
    def __init__(self, rupees, paise=0):
        total_paise = rupees * 100 + paise
        self.rupees = total_paise // 100
        self.paise = total_paise % 100

    def __normalize(self):
        return self.rupees * 100 + self.paise

    def __str__(self):
        return "₹" + str(self.rupees) + "." + str(self.paise)

    def __add__(self, other):
        total = self.__normalize() + other.__normalize()
        return Money(0, total)

    def __sub__(self, other):
        total = self.__normalize() - other.__normalize()
        if total < 0:
            return "Error"
        return Money(0, total)

    def __eq__(self, other):
        return self.__normalize() == other.__normalize()

    def __le__(self, other):
        return self.__normalize() < other.__normalize()

    def __gt__(self, other):
        return self.__normalize() > other.__normalize()

    def __mul__(self, value):
        if type(value) in [int, float]:
            total = int(self.__normalize() * value)
            return Money(0, total)
        return "Error"

    def __truediv__(self, value):
        if value == 0:
            return "Can't divide by 0"
        if type(value) in [int, float]:
            total = int(self.__normalize() / value)
            return Money(0, total)
        return "Error"
        
m1 = Money(100, 50)     
m2 = Money(50, 75) 

print(m1 + m2)          
print(m1 - m2)          
print(m2 - m1)          
print(m1 == m2)  
print(m2 <= m1)       
print(m1 > m2)          
print(m1 * 2)           
print(m1 / 2)           
print(m1 / 0)           