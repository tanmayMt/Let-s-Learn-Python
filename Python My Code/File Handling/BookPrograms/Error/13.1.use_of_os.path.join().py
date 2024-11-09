import os

curpath=os.path.abspath(".")
print("curpath: ",curpath)

os.path.join('/G',"newAddedPath")
print("'newAddedPath' is added successfully")

curpath=os.path.abspath(".")
print("curpath: ",curpath)


if os.path.exists("newAddedPath"):
    print("'newAddedPath' is exists.")
else:
    print("'newAddedPath' is not exists.")