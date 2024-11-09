import os

f=open("12.demo","w")

list1=[30,40,50]
tuple1=(1,2,3,)

f.writelines(list1,"\n")
f.writelines(tuple1)


os.system("cat")