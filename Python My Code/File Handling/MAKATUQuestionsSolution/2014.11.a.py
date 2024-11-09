str1='''"This is only text"\n"Nothing can go wrong"\n"All things are fine..."'''


f=open("G:\\MCA_Techno_1st_semester\\Python Coding\\Python My Code\\File Handling\\MAKATUQuestionsSolution\\Hello.dat","w+")
f.write(str1)
f.seek(0)
print(f.read())

f.close()