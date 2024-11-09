tpl=("Ajoy",23,150)
lst=[23,32,21]
d={'Name':'Dilip','Roll':23}

f=open("3.demo","w")
f.write(str(tpl))
# The write() function takes only string as a argument, 
# not other.That why we need to convert them to string before writing to the file
f.write(str(lst))
f.write(str(d))
f.close()

# f=open("3.demo","r")
# data=tuple(f.readline())
# print(data)