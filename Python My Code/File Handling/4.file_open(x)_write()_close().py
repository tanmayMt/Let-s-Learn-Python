
file=open("1.demo.txt","x") #open the "1.demo.txt" with write(w) mode
txt_input=(input("Write your aim:"))

file.write(txt_input) 
file.close()

file=open("1.demo.txt","r") #open the "1.demo.txt" with read(r) mode
print(file.read(4)) #read the contents of the file
# print(file.read(4)) #read 4 character from the contents of the file