f=open("20.demo","wb")
f.write(b'231')
f.write(b'431')
f.write(b'2632')
f.write(b'833')
f.close()

f=open("20.demo","rb")
buf=f.read()
print("buf= ",buf)

f.seek(0)

f.seek(10,0)
print(f.tell())

f.seek(2,1)
print(f.tell())

f.seek(-5,1)
print(f.tell())

f.seek(-10,2)
print(f.tell())

f.close()