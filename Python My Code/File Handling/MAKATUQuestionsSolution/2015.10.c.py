f=open("G:\\MCA_Techno_1st_semester\\Python Coding\\Python My Code\\File Handling\\MAKATUQuestionsSolution\\file2.txt","r")
lines=f.readlines()

flag="It"
count=0

for line in lines:
    words=line.split()
    for word in words:
        if word==flag:
          count+=1

print("Number of occurences of the pattern 'It': ",count)