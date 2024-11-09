class Student:
    def __init__(self):
        self.name=input("Enter Student Name(Arts): ")

            
    def display(self):
        print(f"Entry No. {self.entry_no}")
        print(f"Student Name: {self.name}")

class Science(Student):
    def __init__(self):
        super().__init__()
        self.phy=int(input("Enter the marks in Phy: "))
        self.chem=int(input("Enter the marks in chem: "))
        self.mat=int(input("Enter the marks in mat: "))
    def display(self):
        super().display(entry_no)
        print(f"Phy: {self.phy}\tChem: {self.chem}\tMath: {self.mat}")
    print()

class Arts(Student):
    def __init__(self):
        super().__init__()
        self.eng=int(input("Enter the marks in Eng: "))
        self.his=int(input("Enter the marks in His: "))
        self.eco=int(input("Enter the marks in Eco: "))
    def display(self):
        super().display()
        print(f"Eng: {self.eng}\tHis: {self.his}\tEco: {self.eco}")
    print()

entry_no=int(input("Enter Entry No:"))
if entry_no == 1:
    s1=Science(entry_no)
    s1.display()
elif entry_no == 2:
    s2=Arts(entry_no)
    s2.display()
else:
    print("Error!!")
