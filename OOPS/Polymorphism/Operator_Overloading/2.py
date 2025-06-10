class Student:
    
    def __init__(self, name, marks):
        
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks
    
s1 = Student("Kalp", 90)
s2 = Student("Vidhi", 90)

print(s1 == s2)