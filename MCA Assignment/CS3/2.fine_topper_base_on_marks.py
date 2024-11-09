'''
Write a python program that will accept the names of students 
and a list of marks in 4 subjects using dictionary. Create 
another dictionary from this dictionary that has name of the 
students and their total marks. Also find the topper and 
his/her name.	
'''
num=int(input("Enter total number of student: "))
print()

std_marksheet={}
std_total_marks={}

for i in range(1,num+1):
    print()
    name=input(f"{i}.Enter the name of the student: ")
    print(f"  Enter marks of student({name}): ")

    std_marksheet.update({name:[int(input("  Sub1: ")),
                                int(input("  Sub2: ")),
                                int(input("  Sub3: ")),
                                int(input("  Sub4: "))
                               ]
                         }
                        )
    all_marks=std_marksheet.get(name) # list type
    total=sum(all_marks)
    std_total_marks.update({name:total})

print("\nStudents name and their marks: ",std_marksheet)
print("Students name and their total mark: ",std_total_marks)

value=list(std_total_marks.values())
key=list(std_total_marks.keys())

index_max=value.index(max(value))
topper=key[index_max]

print(f"\n{topper} is the topper(Marks:{value[index_max]})\n")