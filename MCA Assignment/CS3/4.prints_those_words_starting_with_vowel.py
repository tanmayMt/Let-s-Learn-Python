'''
 Write a python program that prints only those words starting 
 with a vowel.
'''

my_list = ["Abc", "phy", "and", "okay", "educate", "learn", "code"]
print("The original list of words:",my_list)

my_vowel = "aeiouAEIOU"
print("The vowels are ",my_vowel)

result = []

for i in my_list:
   flag = False
   for element in my_vowel:
      if i.startswith(element):
         flag = True
         break
   if flag:
      result.append(i)

print("The words starts with vowels: ",result)