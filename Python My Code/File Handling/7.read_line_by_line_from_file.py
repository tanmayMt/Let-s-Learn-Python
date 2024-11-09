
file=open("5.demo.txt","w") 

file.write("Hello\nGood Morning\nHow are you") 
file.close()

file=open("5.demo.txt","r") 
print(file.readline()) #read the contents of the file line by line
print(file.readline())
print(file.readline())
file.close()