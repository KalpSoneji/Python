class Gov:
    rulingParty = "BJP" # class level variable
    
    def __init__(self):
        print("Gov class default constructor")
    
    def applyTax(self):
        self.tax = 10 #instance variable... Gov    


class StateGov(Gov):
    
    def __init__(self):
        print("state gov const called..")
    
    def getTax(self):
        print(f"tax from gov = {self.tax}")    



s = StateGov()  # state class default constructor...
s.applyTax()    # parent    
s.getTax()      # child
    
                