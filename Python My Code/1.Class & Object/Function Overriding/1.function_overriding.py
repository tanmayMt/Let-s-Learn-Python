
class Parent:
    def __init__(self):
        self.value="Inside Parent class"
    def display(self):
        print(self.value)

class Child(Parent):
    def __init__(self) :
        self.value="Inside Child class"
    def display(self):
        print(self.value)

obj2=Child()
obj2.display()


# print(obj2.value)
