import os

curpath=os.path.abspath(".")

os.path.join('.',"newAddedPath")
print("'newAddedPath' is added successfully")

if os.path.exists("newAddedPath"):
    print("'newAddedPath' is exists.")
else:
    print("'newAddedPath' is not exists.")