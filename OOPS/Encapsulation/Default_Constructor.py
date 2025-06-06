class Bank:

    def __init__(self):

        print("Constructor called")
        self.name = "SBI"
        self.IFSC = "SBIN123"

    def detail(self):
        print("Bank name = ", self.name)
        print("Bank IFSC = ", self.IFSC)

SBI = Bank()
SBI.detail()

HDFC = Bank()
HDFC.detail()