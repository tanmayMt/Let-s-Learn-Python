# String Data Type
# A string is a ordered sequence of characters.

# Assign string to a variable
str1 = 'Hello'
print('str1=', str1)

# Use of different type of quotes to assign a string value
# double quotes
str2 = "'Tomorrow will be better than today'--- Modi"
print('str2=', str2)

# triple quotes
str3 = '''"Tomorrow will be better than today"--- Modi'''
print('str3=', str3)

# When can assign a multiline string to variable is done by triple quotes(''' '')
str4 = '''My name
is
Anish
Roy
'''
print('str4=', str4)

# String Indexing
str5 = 'Hello World'
#       012345678910    <-- indexing of string
print('str5[0]:', str5[0])
print('str5[3]:', str5[3])
print('str5[-1]:', str5[-1])  # Negative Indexing
print('str5[-3]:', str5[-3])  # Negative Indexing
print('str5[1:3]:', str5[6:11])  # access the substring from the given string by using slicing operator :( colon).

# String Slicing using range slicing operator.
str6 = "Hello Brother"
print(str6[6:13])  # Brother
print(str6[6:13:2])  # Bohr

# Reverse of a string
str7 = "Hello Brother"
print(str7[::-1])  # it is use for reverse of a string

# String Slicing using slice() function
str8 = "This is my Python Tutorial "
slice1 = slice(-9, -1)
print(str8[slice1])  # Tutorial
sliceObject = slice(8, -1)
print(str8[sliceObject])

# String length
str9 = "Hello World"
lengthOfstr9 = len(str9)
print("Length of str9= ", lengthOfstr9)  # Length of str9=  11
