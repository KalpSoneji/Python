class Student:
    
    collegeName = "GUJARAT UNI" #class level variable...
    
    def getStudentName(self,name):
        #name = local bariable...
        #self.name = instance variable.
        self.name = name
        #pass

stu = Student #() is optional in this case      
stu.getStudentName("RAM")
print(f"College name = {stu.collegeName} \nStudent name  = {stu.name}")