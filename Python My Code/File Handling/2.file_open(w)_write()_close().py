
file=open("1.demo.txt","w") #open the "1.demo.txt" with write(w) mode
txt_input=(input("Write Content for file:"))

file.write(txt_input) 
file.close()

file=open("1.demo.txt","r") #open the "1.demo.txt" with read(r) mode
print(file.read()) #read the contents of the file
# print(file.read(4)) #read 4 character from the contents of the file
