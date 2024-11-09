f=open("8.demo","r")
print("Seek Possition before read: ",end='')
print(f.tell())

buf=f.read()
print("Content of the file:")
print(buf)

print("Seek Possition after read: ",end='')
print(f.tell())

f.seek(-2,2)
print(f.tell())
