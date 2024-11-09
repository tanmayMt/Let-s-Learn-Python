import re
str=input("Enter a sentance: ")


''' Accept one or more sentences and store the words in a list using 
    delimiters [ ! , ? . ; blank space ] and sort the words '''


words=re.split(r"[!*!@#$%^&?()><:;\"\s\s]",str)
print(words)