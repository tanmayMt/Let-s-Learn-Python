#The split() function returns a list where the string has been split at each match
import re

txt1="Hi My name is Rohan sen.I am 23 year old."

#Split at each white-space character
words1=re.split("\s",txt1)# Here \s means space 

print(words1)



#You can control the number of occurrences by specifying the maxsplit parameter:

txt2="Hi My name is Rohan sen.I am 23 year old."

#Split the string only at the first occurrence:
words2=re.split("\s",txt2,1)

print(words2)