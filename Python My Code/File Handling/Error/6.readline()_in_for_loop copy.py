file=open("5.demo.txt","w") 

file.write("Hello\nGood Morning\nHow are you") 
file.close()

file=open("5.demo.txt","r")
for i in file:
    print(file.readline()) #Only 'Good Morning' is diaplaying
file.close()