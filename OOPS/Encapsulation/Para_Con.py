class University:

    uni_name = "GTU"

    def __init__(self, clgName):
        self.clgName = clgName

    def print(self):
        print(f"{self.clgName} is registered under {University.uni_name}")

GLS = University("GLS")
GLS.print()