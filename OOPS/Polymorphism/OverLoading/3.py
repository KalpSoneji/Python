class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")


class C(B,A):
    pass

obj = C()
# obj.show(100)
obj.show()
            