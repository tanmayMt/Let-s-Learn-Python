'''
1.Write a program that uses class to store the name and marks in 4 
subjects of students. Use the list to store the marks in 4 subjects. 
Also find the total marks of the students and find the name of the 
student who have obtained the highest total marks.
'''

class Student:
    std_total_marks={} #class data memeber

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_total_marks(self):
        self.total=sum(self.marks)
        Student.std_total_marks.update({self.name:self.total})


    #Class method
    def display_name_total_marks():
        print("Students name and their total marks:",Student.std_total_marks)

    def find_topper():
        value=list(Student.std_total_marks.values())
        key=list(Student.std_total_marks.keys())
        max_index=value.index(max(value))
        topper=key[max_index]
        print(f"{topper} obtained the highest total mark (Marks:{value[max_index]})\n")



num=int(input("Enter how many student are there? : "))
print()

for i in range(1,num+1):
    print()
    name=input(f"{i}.Enter the name of the student: ")
    print(f"  Enter marks of student ({name}): ")
    marks=[
           int(input("   Sub1: ")),
           int(input("   Sub2: ")),
           int(input("   Sub3: ")),
           int(input("   Sub4: "))
          ]
    std=Student(name,marks)
    std.calculate_total_marks()

Student.display_name_total_marks()
Student.find_topper()