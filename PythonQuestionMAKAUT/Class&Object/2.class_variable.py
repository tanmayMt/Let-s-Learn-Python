class Student:
    stream='CSE'  #Class Variable

    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def display(self):
        print('Roll: ',self.roll)
        print('Name: ',self.name)
        print('Stream: ',Student.stream)
        print()

s1=Student(10,'Ronit Roy')
s2=Student(11,'Arohi Sen')

s1.display()
s2.display()


Student.stream='II'

s1=Student(10,'Ronit Roy')
s1.display()