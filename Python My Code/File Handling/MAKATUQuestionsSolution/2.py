def read():
    f=open("G:\\MCA_Techno_1st_semester\\Python Coding\\Python My Code\\File Handling\\MAKATUQuestionsSolution\\Poem.txt","r")

    lines=f.readlines()
    for line in lines:
        if line[0] == 'F':
            print(line,end='')
read()