
file=open("6.demo.txt","w") #open the "1.demo.txt" with write(w) mode

file.write("Hello")
file.write("Good Morning") 
file.write("How are you") 

file.close()

file=open("6.demo.txt","r") #open the "1.demo.txt" with read(r) mode
print(file.readline()) #read the contents of the file line by line
# print(file.readline())
# print(file.readline())
file.close()

# file=open("4.demo.txt","r")
# for i in file:
#     print(file.read())