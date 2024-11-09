import json

nestedList=[100,[60,40],100,[50,50]]
f=open("18.demo","w+")
json.dump(nestedList,f)

f.seek(0)

nestedList2=json.load(f)
print("nestedList2: ",nestedList2)
