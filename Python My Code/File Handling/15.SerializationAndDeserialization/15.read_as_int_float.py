f=open("4.1.demo.txt","w+")

numint=23
numfloat=56.45

f.write(str(numint)+"\n")
f.write(str(numfloat))

intnum=int(f.readline())
floatnum=float(f.readline())
print("intnum= ",intnum)
print("floatnum= ",floatnum)

f.close()