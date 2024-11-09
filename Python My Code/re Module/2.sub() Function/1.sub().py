import re

#The sub() function replaces the matches with the text of your choice:
txt="My name is Rohit Sen"

words=re.sub("\s","_",txt) #space will replace by _

print(words)



#You can control the number of replacements by specifying the count parameter
txt="My name is Rohit Sen"

words=re.sub("\s","_",txt,2)#Replace the first 2 occurrences
print(words)