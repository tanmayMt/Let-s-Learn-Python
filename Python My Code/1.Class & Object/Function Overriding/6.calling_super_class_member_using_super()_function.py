class Parent:
    def display(self):
        print("Inside Parent class")

class Child(Parent):
    def display(self):
        super().display()
        print("Inside Child class")


obj=Child()
obj.display()
