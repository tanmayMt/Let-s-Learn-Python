'''
str = input('Enter a sentence ')

# ordinary split() function using blank space as delimiter
words = str.split()
print(words) '''

''' Accept one or more sentences and store the words in a list using 
    delimiters [ ! , ? . ; blank space ] and sort the words '''
    
import re

str = input('Enter a sentence ')
print(str)
# advanced split() function using multiple delimiters ie, ! , ? . ; blank space
words = re.split(r'[!,?.;\s*]', str)
print('Before sorting the words are:')
print(words)

words.sort()
print('After sorting the words are:')
print(words)