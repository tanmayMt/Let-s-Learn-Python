'''
   4.Write a python program which will keep track of the stock of books
   available in the library. In this program, you will have to use the
   add( ) to add the books, and also the display( ).
'''
import datetime

class Libaray:
   total_list_of_books=[]
   def add(self):
      self.name=input("Enter Book Title: ")
      self.author=input("Enter Author Name: ")
      self.number_of_copy=int(input("No of Book: "))
      self.cur_date=datetime.date.today()
      self.book_details=[self.name,self.author,self.number_of_copy,self.cur_date]
      Libaray.total_list_of_books.append(self.book_details)

   def display(self):
      print(" List of Books Avlailable in Libaray ")
      
      for i in Libaray.total_list_of_books:
         print(f"  Title: {i[0]}")
         print(f"  Author: {i[1]}")
         print(f"  No of Books Avl: {i[2]}")
         print(f"  Added on: {i[3]}\n")


l1=Libaray()
while(True):
    print(" --------------------------------------------------------------------------------")
    print("|\tPress 1: Add Book\tPress 2: Display Books\t\tPress 3: Exit\t|")
    print(" --------------------------------------------------------------------------------")
    choice=int(input("Enter your choice: "))

    if choice == 1:
        print()
        l1.add()
        print()
    elif choice == 2:
        print()
        l1.display()
        print()
    elif choice == 3:
        exit()
    else:
        print("Wrong Choice!!!!!!!")