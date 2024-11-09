f=open("5.demo","r")
while True:
    data=f.readline()
    if data=='':
        break
    print(data,end='')