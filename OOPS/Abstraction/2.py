#ABC abstract base class
from abc import ABC,abstractmethod 

# Abstract Class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(slef):
        pass
    
    def test(self):
        print("test....")

v = Vehicle()
v.start_engine()

# since the method is empty, it throws error