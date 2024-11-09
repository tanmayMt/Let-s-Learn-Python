class GrandParent:
    def display(self):
        print('In Grand Parent Class')

class Parent1(GrandParent):
    def display(self):
        print('In Parent1 Class')

class Parent2(GrandParent):
    def display(self):
        print('In Parent2 Class')

class Child(Parent1,Parent2):
    def display(self):
        super().display()
        Parent1.display(self)
        Parent2.display(self)
        print('In Child Class')
        print(Child.__mro__)

c1=Child()
c1.display()
