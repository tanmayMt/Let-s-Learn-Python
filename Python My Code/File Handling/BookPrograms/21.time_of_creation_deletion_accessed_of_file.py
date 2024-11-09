import os,time

f="20.demo"
print(f)

created=os.path.getctime(f)
print("Date created: ", time.ctime(created))

modified=os.path.getmtime(f)
print("Date modified: ",time.ctime(modified))

accessed=os.path.getatime(f)
print("Date Accessed: ",time.ctime(accessed))