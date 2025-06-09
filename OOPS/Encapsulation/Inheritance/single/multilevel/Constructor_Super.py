class India:
    
    def __init__(self):
        self.country = "India"
        print("India class default constructor called")
    
    def indian(self):
        print("Indian method called")    

class Gujarat(India):
    
    def __init__(self):

        super().__init__() # invoking India class constructor
        self.state = "Gujarat"
        print("Gujarat class Constructor called")        
    
    def Gujarati(self):
        print("Gujarati method called")    
        print(f"Country name = {self.country}")

class Ahmedabad(Gujarat):
    
    def __init__(self):
        super().__init__() # invoking Gujarat class constructor
        self.city = "Ahmedabad"
        print("Ahmedabad class constructor called")
    
    def Ahmedabadi(self):
        print("Ahmedabad method called")        
        print(f"Country name = {self.country} State name  = {self.state}")

a = Ahmedabad()        
a.Gujarati()
a.Ahmedabadi()
        
    