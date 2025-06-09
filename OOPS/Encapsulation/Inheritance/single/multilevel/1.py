class Xabi:

    def details1(self):
        print("1st Gen")

class Iniesta(Xabi):

    def details2(self):
        print("2nd Gen")

class Yamal(Iniesta):

    def details3(self):
        print("3rd Gen")

new = Yamal()
print(new.details1())
print(new.details2())
print(new.details3())