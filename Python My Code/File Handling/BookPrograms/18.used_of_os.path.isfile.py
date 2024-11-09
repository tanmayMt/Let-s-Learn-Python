import os

print(os.path.isfile("16.demo"))

if os.path.isfile("16.demo"):
    print("'16.demo' is exists")
else:
    print("'16.demo' doesn't exists")