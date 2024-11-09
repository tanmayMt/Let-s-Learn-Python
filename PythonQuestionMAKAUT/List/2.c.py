#insert 9 at begin 
l=[5,4,7,3,6,2,1]
c=l
l=[9]
l.append(map(int,list(*c)))
print(l)
