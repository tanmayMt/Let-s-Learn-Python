class Parent:
    def __init__(self):
        self.p=100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.c=Parent.p+50
    def display(self):
        print("c= ",self.c)

c1=Child()
c1.display()