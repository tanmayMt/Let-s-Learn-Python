class CollageStudent:
    name="Raj Collage"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def collage_name(cls):
        print("(Class Method)",cls.name)
    
    #Instance Method
    def collage_student(self):
        print("(Instance Method)",self.name,self.age)
    
    @staticmethod
    def student_age(age):
        print("(This is static method)age: ",age)

name="Anish Sen"
age=22

s1=CollageStudent(name,age)
s2=CollageStudent("Joy",12)

#Calling @classmethod using instance/object of the class
s1.collage_name()

#Calling Instance Method using instance/object of the class
s2.collage_student()

#Calling @staticmethod using instance/object 's2' of the class
s1.student_age(age)

#Calling @staticmethod using class name
CollageStudent.student_age(age)




    