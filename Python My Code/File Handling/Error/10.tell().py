file=open("10.demo.txt","w")
file.write("Hello\nGood") 
file.close()

file=open("10.demo.txt","r")
print("Content of the file '9.demo.txt'---")
print(file.read())
print("Current Possition: ",file.tell())
file.close()

file=open("10.demo.txt","w+") # error tell() function return 0 when we use options r w
file.seek(7)
print("Current Possition: ",file.tell())

print("After Change:",file.write("Ba"))


for i in file:
    i.replace("Good","bad")

file.close()