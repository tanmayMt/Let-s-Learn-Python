'''
   2.Write a program which will use the class "Account". In this class, you have to use
     deposit() , withdraw( ) and balance_enquiry( ).
 '''


import datetime

class Account:
    def cur_date():
        return (datetime.date.today())
    def cur_time():
        return (datetime.datetime.now()).strftime("%X")


    def __init__(self,acc_no,name):
        self.acc_no=acc_no
        self.name=name
        self.balance = 0
        
    def deposit(self):
        amount = float(input("\nEnter the amount to be deposit: "))
        self.balance = self.balance + amount

        cur_date=Account.cur_date()
        cur_time=Account.cur_time()

        print (f"Your A/C {self.acc_no} is credited with Rs.{amount} on {cur_date} at {cur_time}. Avl Balance: Rs.{self.balance}\n")
    
    def withdraw(self):
        amount = float(input("\nEnter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            cur_date=Account.cur_date()
            cur_time=Account.cur_time()
            print (f"Your A/C {self.acc_no} is debited with Rs.{amount} on {cur_date} at {cur_time}. Avl Balance: Rs.{self.balance}\n")
        else:
            print ('Insuficient Balance!!!\n')
    
    def enquiry(self):
        print (f"\nAvlailable Balance: {self.balance}\n")
        

acc_no=input("Enter the Account No. ")
name=input("Enter the name of the account holder: ")
print("\n\n")

acc = Account(acc_no,name)
while(True):
    print(" ---------------------------------------------------------------------------------------------------------------")
    print("|\tPress 1: For Credit\tPress 2: For Debit\tPress 3: For Balance Enquiry\tPress 4: For Exit\t|")
    print(" ---------------------------------------------------------------------------------------------------------------")
    choice=int(input("Enter your choice: "))

    if choice == 1:
        acc.deposit()
    elif choice == 2:
        acc.withdraw()
    elif choice == 3:
        acc.enquiry()
    elif choice == 4:
        exit()
    else:
        print("Wrong Choice!!!!!!!")