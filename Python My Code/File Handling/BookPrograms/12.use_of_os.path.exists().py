import os

if os.path.exists("12.myFolderc"):
    print("'12.myFolderc' is already exists")
else:
    print("'12.myFolderc' is not exists")
    c=input("Enter 'c' to create the directory:")
    if (c=='c'):
        os.mkdir("12.myFolderc")