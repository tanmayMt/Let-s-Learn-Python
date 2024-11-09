'''
   5. Write a python program that will accept the code and price of 5 items
      in a list. The user will give the quantity as input. Display the total
      billing as like :
      Code Price Quantity TotalAmt
'''

class Product:

    def __init__(self):
        self.code=[]
        self.price=[]
        self.c=0
        self.qty=0
        self.amount=int(0)
        self.sold_code=[]
        self.sold_price=[]
        self.sold_qty=[]
        self.sold_total=[]
    def accept_item(self):
        print("Enter the Item Codes and Price: ")
        for i in range(0,3):
            self.code.append(int(input(f" Enter Code for item no.{i+1}: ")))
            self.price.append(int(input(f" Enter Price for item no.{i+1}: ")))
            print()

    def display(self):
        # print("Item's Code are: ",self.code)
        for i in self.sold_code:
            key=self.code.index(i)
            key1=self.sold_code.index(i)
            print(f'{i}\t{self.price[key]}\t{self.sold_qty[key1]}\t{self.sold_total[key1]}')
        print(f'Total Amt: {self.amount}')
        

    def search(self,c):
        for i in range(0,3):
            if c == self.code[i]:
                # print(f"Fond at {i}")
                return (self.price[i])
        print("Item is not found!!")
        return 0

    def sales(self):
        while(True):
            self.c=int(input("Enter the Item Codes you want to purshase: "))
            p=self.search(self.c)
            if p==0:
                continue
            # print("Price of the item is ",p)
            self.sold_code.append(self.c)
            self.qty=int(input("Enter the Quantity: "))
            self.sold_qty.append(self.qty)
            self.amount=self.amount+p*self.qty
            self.ans=input("Do you want to continue?Y/N : ")
            if self.ans=='n' or self.ans=='N':
                break
        print(f"Total: {self.amount}")
p1= Product()


while(True):
    print('------------------------------------------------------------------------------')
    print("| 1:Accept Code & Price \t2:Sales\t3:Print Bill\t4:Exit |")
    print('------------------------------------------------------------------------------')
    choice=int(input("Enter your choice: "))

    if choice == 1:
        print()
        p1.accept_item()
        print()
    elif choice == 2:
        print()
        p1.sales()
        print()
    elif choice == 3:
        print()
        p1.display()
        print()
    elif choice == 4:
        print("Thank You. Visit Again")
        exit()
    else:
        print("Wrong Choice")