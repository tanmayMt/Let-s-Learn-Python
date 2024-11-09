class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        self.a=self.a+o.a
        return A(self.a)
        # sum=self.a+o.a
        # return A(sum)
        #it is more sensible to return a object .

obj1=A(10)
obj2=A(5)

obj3=obj1+obj2
# print(obj3.a)
print(obj3) #Why this give an error message






w="Dho"
x="ni"
z=w+x
print(z)