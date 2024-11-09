#using copy() deep copy
print("\nusing copy() deep copy")
l1=[3,5,7,9]
l2=l1.copy() #deep copy
print(f"Id of l1({id(l1)}) and l2({id(l2)}) are same?: {l1 is l2}")
print("l1:",l1)
print("l2:",l2)

#using copy.deepcopy() deep copy
import copy
print("\nusing copy.deepcopy()")
l3=[3,5,80,7,9]
l4=copy.copy(l3) #deep copy
print(f"Id of l1({id(l3)}) and l2({id(l4)}) are same?: {l3 is l4}")
print("l1:",l3)
print("l2:",l4)

#using copy.copy() sallow copy
import copy
print("\nusing copy.copy()")
l5=[3,5,51,7,9]
l6=copy.copy(l5) #deep copy
print(f"Id of l1({id(l5)}) and l2({id(l6)}) are same?: {l5 is l6}")
print("l1:",l5)
print("l2:",l6)

#using assignment operator
print("\nUsing assignment(=) operator: ")
l7=[3,5,7,19]
l8=l7   # Sallow copy
print(f"Id of l1({id(l7)}) and l2({id(l8)}) are same?: {l7 is l8}")
print("l1:",l7)
print("l2:",l8)

#Uing append() method
print("\nUing append() method")
li1=[5,7,8]
li2=[]
for i in li1:
    li2.append(i)
print(f"Id of li1({id(li1)}) and li2({id(li2)}) are same?: {l7 is l8}")
print("l1:",li1)
print("l2:",li2)

#Uing map() method
print("\nUing map() method")
li3=[6,8,9]
li4=list(map(int,li3))
print(f"Id of li1({id(li3)}) and li2({id(li4)}) are same?: {l3 is l4}")
print("l1:",li3)
print("l2:",li4)

#Uing slice() method
print("\nUing slice() method")
lis=[6,8,9]
lis1=lis[slice(len(lis))]
print(f"Id of lis({id(lis)}) and li2({id(lis1)}) are same?: {lis is lis1}")
print("lis:",lis)
print("lis1:",lis1)