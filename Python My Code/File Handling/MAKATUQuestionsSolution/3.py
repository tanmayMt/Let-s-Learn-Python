def big_lines():
    f=open("G:\\MCA_Techno_1st_semester\\Python Coding\\Python My Code\\File Handling\\MAKATUQuestionsSolution\\Poem.txt","r")
    lines=f.readlines()
    for line in lines:
        if len(line) > 9:
            print(line,end='')
    f.close()

big_lines()