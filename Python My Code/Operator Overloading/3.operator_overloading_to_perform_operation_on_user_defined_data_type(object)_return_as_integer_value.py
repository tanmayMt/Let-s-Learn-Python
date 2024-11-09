class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        # self.a=self.a+o.a
        # return A(self.a)

        self.a=self.a+o.a
        return self.a

obj1=A(10)
obj2=A(5)

obj3=obj1+obj2  #calling __add__ function for operator overloading

print(obj3)
