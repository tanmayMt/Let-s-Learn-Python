# variable are a temporary memory location to store values.
# Unlike other programming language, Python has no command for declaring a variable.
a = 15 # hare a is a variable
print('a=', a)

num1 = 30
num1 = 40 # re-declaration of variable 'num'
print('num=', num1)

# Concatenation of variable
str1 = 'Study'
str2 = 'Tonight'
str3 = str1 + str2
print('str3=', str3)

# Local and Global variable
a = 10
def display():
    b = 20
    print('Local variable:', b)
    print('Global variable:', a)
display()

# how to delete a variable
num = 67
print("num=", num)
del num
print("after use del keyword:", num)