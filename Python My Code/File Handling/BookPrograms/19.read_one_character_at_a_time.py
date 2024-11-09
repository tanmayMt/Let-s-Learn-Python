f=open("19.demo","r")
while True:
    buf=f.read(1) # reads 1 character from a file object f
    if buf=='':   # read() return empty string on reaching end of file
        break
    print(buf,end='')
f.close()