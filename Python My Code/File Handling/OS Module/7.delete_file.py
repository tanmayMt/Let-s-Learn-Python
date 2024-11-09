import os

file=open("7.demo.txt","w")
txt_input=input("Enter the contents for '7.demo.txt' file: ")
file.write(txt_input)
file.close()

file=open("7.demo.txt","r")
print(file.read())
file.close()

os.remove("7.demo.txt")

# file=open("7.demo.txt","r")
# print(file.read())
# file.close()