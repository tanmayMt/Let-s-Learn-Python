file=open("4.demo.txt","w") #open the "1.demo.txt" with write(w) mode
file.write("Hello\nGood Morning\nHow are you")#unable to print "Hello" word
#file.write("\nHello\nGood Morning\nHow are you")
file.close()

file=open("4.demo.txt","r")
for i in file:
    print(i)

file.close()