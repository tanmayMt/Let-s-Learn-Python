'''Write a program that prompts the user to enter a file name. 
Open the file and print the frequency of each word in it.'''

file_name=input("Enter the file name you want to open: ")
f=open(file_name)

list2= []
for i in f:
    list1=i.split()
    for j in list1:
        list2.append(j)

set_list=set(list2)

# print("list2:",list2)
# print("set_list: ",set_list)

for word in set_list:
    c=list2.count(word)
    print(f"Frequency of {word} is {c}")

f.close()