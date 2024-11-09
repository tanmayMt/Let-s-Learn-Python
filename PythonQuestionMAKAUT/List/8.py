

#using copy.deepcopy() deep copy
import copy
print("\nusing copy.deepcopy()")
l3=[3,5,80,7,9]
l4=copy.copy(l3) #deep copy
print(f"Id of l1({id(l3)}) and l2({id(l4)}) are same?: {l3 is l4}")
print("l1:",l3)
print("l2:",l4)
    
#using copy.copy() sallow copy
print("\nusing copy.copy() sallow copy")
l5=[3,5,51,7,9]
l6=copy.copy(l5) #deep copy
print(f"Id of l1({id(l5)}) and l2({id(l6)}) are same?: {l5 is l6}")
print("l1:",l5)
print("l2:",l6)

#using append() method
print("\nUsing append() method")
l1=[4,7,5,8]
l2=[]
l2.