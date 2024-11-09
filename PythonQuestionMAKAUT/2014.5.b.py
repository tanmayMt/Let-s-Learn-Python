import copy
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return (f"Name:{self.name}  Age:{self.age}")


p1=Person("Roni",21)
print("p1: ",p1)
print(f"ID of p1: {id(p1)}\n")

# p2=p1
p2=copy.deepcopy(p1)
print("p2: ",p1)
print(f"ID of p1: {id(p2)}\n")