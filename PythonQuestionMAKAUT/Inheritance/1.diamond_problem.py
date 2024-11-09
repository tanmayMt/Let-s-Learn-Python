class GrandParent:
    def display(self):
        print('In Base Class')

class Parent1(GrandParent):
    def display(self):
        print('In Parent1 Class')

class Parent2(GrandParent):
    def display(self):
        print('In Parent2 Class')

class Child(Parent1,Parent2):
    def display(self):
        print('In Child Class')

c1=Child()
c1.display()