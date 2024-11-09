
file=open("3.demo.txt","w") #open the "3.demo.txt" with append(w) mode
txt_input=(input("Write your aim:"))

file.write(txt_input) 
file.close()

file=open("3.demo.txt","rb") #open the "3.demo.txt" with read(r) mode
print(file.read()) #read the contents of the file