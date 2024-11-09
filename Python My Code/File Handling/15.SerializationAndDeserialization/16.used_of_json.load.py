import json

# list1=[10,20,30,40,50]
# f=open("15.demo","w+")
# json.dump(list1,f)

# f.seek(0)

# list2=json.load(f)

# print("list2= ",list2)
# f.close()




tuple1=(23,45,"Hello")

f=open("16.2.demo.txt","w+")
json.dump(tuple1,f)

f.seek(0)

tuple2=json.load(f)


print("tuple2= ",tuple2)
print(type(tuple2))

print(tuple(tuple2))
