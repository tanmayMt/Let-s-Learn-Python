class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        self.a=self.a+other.a
        self.b=self.b+other.b
        return Complex(self.a,self.b)


obj1=Complex(2,3)
obj2=Complex(3,4)

obj3=obj1+obj2

print(obj3.a,obj3.b)
