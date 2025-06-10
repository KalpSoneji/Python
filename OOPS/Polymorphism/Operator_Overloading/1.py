class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, others):
        return self.pages - others.pages

b1 = Book(100)
b2 = Book(200)

b3 = b1 + b2
print(b3)

b4 = b2 - b1
print(b4)

