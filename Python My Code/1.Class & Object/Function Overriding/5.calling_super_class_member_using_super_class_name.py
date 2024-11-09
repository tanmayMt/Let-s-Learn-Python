class Parent:
    def display(self):
        print("Inside Parent class")

class Child(Parent):
    def display(self):
        Parent.display(self)#why we need pass self as a arguments
        print("Inside Child class")


obj=Child()
obj.display()
