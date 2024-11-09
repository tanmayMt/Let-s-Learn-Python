
class A:
    def __init__(self,a):
        self.a=a
    
obj1=A(3)
obj2=A(7)
print(type(obj1))
print(type(obj2))

obj=obj1+obj2

print(obj.a)