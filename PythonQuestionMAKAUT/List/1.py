import copy
l1=[1,2,3,4,5]
l2=copy.deepcopy(l1)

#after modifing in list 'l1' made affect on 'l2' object -Why?

l1.append(7)

print("l1: ",l1)
print("l2: ",l1)

#Althrough id of this two object are different
print("l1 id: ",id(l1))
print("l2 id: ",id(l2))