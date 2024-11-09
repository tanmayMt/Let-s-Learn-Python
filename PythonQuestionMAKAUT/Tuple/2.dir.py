d={101:'Python',102:'C',103:'DS'}

for i,(k,v) in enumerate(d.items()):
    print(i,k)

d[101]="Ruby"
print(d)

del(d[101])
print(d)

print(d.values())