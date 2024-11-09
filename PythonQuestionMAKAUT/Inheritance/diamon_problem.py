class GrandParent:
    def display(self):
        print('In GrandParent')

class Parent1(GrandParent):
    def display(self):
        super().display()
        print('In Parent1')

class Parent2(GrandParent):
    def display(self):
        super().display()
        print('In Parent2')

class Child(Parent1,Parent2):
    def display(self):
        super().display()
        print('In Child')
        print('After use of __mro__:')
        print(Child.__mro__)
        

c1=Child()
c1.display()
