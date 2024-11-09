a={1,3,8,4,9,5}
b={2,4,6,8,10}

u=a.union(b)
print(u)

i=a.intersection(b)
print(i)

d=a.difference(b)
print(d)

syd=a.symmetric_difference(b)
print(syd)

dj=a.isdisjoint(b)
print(dj)



a={1,2}
b={4,6,8}
print(a.isdisjoint(b))