
file=open("2.demo.txt","a") #open the "1.demo.txt" with append(w) mode
txt_input=(input("Write your aim: "))

file.write(txt_input) 
file.close()

file=open("2.demo.txt","r") #open the "1.demo.txt" with read(r) mode
print(file.read()) #read the contents of the file