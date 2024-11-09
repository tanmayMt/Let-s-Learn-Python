class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        obj=self.a+o.a
        print(type(obj))
        return obj
        # sum=self.a+o.a
        # return A(sum)

obj1=A(10)
obj2=A(5)

obj3=obj1+obj2
print(obj3)
# print(obj3.a)