def read():
    f=open("G:\\MCA_Techno_1st_semester\\Python Coding\\Python My Code\\File Handling\\MAKATUQuestionsSolution\\Poem.txt","r")
    while True:
        line=f.readline()
        if line == '':
            break
        else:
            print(line,end='')
    f.close()
read()