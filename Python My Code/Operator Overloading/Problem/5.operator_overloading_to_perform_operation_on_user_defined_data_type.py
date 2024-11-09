class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        self.a=self.a+o.a
        return A(self.a)

        # self.a=self.a+o.a
        # return self.a

obj1=A(10)
obj2=A(5)

obj3=5+int(obj2)  #calling __add__ function for operator overloading

# print(obj3.a)
#print(obj3)  #<__main__.A object at 0x00000227703DFCD0>