import re

# words which start with 'the'
print(re.findall('^the','the word is complex,the there'))

# match only with words 'the'
print(re.findall('the','the word is compthelex,the there'))

# any string which contains 'the' but does not begin with 'the'
print(re.search('[^the*$the]',"the sdfbsdathe"))