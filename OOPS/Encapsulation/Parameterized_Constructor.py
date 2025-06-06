class Bank:

    def __init__(self, name, IFSC):
        self.name = name
        self.IFSC = IFSC

    def detail(self):
        print("Bank name = ", self.name, "\nIFSC = ", self.IFSC)

SBI = Bank("SBI", "SBIN007")
SBI.detail()

Axis = Bank("Axis", "AXIS007")
Axis.detail()

    