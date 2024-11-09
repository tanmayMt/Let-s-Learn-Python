file=open("9.demo.txt","w")
file.write("Hello\nGood") 
file.close()

file=open("9.demo.txt")
print("Content of the file '9.demo.txt'---")
print(file.read())
print("Current Possition: ",file.tell())
file.close()

file=open("9.demo.txt","r") # error tell() function return 0 when we use options r w
print("Current Possition: ",file.tell())
#file.seek(7)
# print("After Change:",file.write("Ba"))
file.close()