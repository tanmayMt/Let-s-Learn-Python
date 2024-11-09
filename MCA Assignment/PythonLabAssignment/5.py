'''
   5. Write a python program that will accept the code and price of 5 items
      in a list. The user will give the quantity as input. Display the total
      billing as like :
      Code Price Quantity TotalAmt
'''

import datetime

class Product:
    code=1000
    total_list_of_products=[]
    sold_products=[]
    all_product_code=[]
    total=0
    def add(self):
        self.code=self.code+1
        self.name=input("Enter Product Name: ")
        self.price_per_pic=int(input("Enter Price Per Pic : "))
        self.product_details=[self.code,self.name,self.price_per_pic]
        Product.total_list_of_products.append(self.product_details)

    def display(self):
        print(" List of Products Avlailable in Store \n")
        print(f"\tCode\t      Product\t  Price/Unit")
        for i in Product.total_list_of_products:
            for j in i:
                print(f"\t{j}\t",end="")
            print()
    
    def create_invoice(self):
        self.cus_name=input("Enter Customer Name: ")
        print()
       
        #Collecting all the code of the product
        for j in Product.total_list_of_products:
            Product.all_product_code.append(j[0])

        for i in range(0,5):
            self.code=int(input("Enter Product Code: "))
            if self.code in Product.all_product_code:
            
                for i in Product.total_list_of_products:
                    if self.code == i[0]:
                        self.quantity=int(input("Enter Quantity: "))
                        self.item_price=i[2]*self.quantity
                        Product.total=Product.total+self.item_price
                        item=list(i)
                        item.append(self.quantity)
                        item.append(self.item_price)
                        Product.sold_products.append(item)
            else:
                print("Invaild Invoke No.!!\n")
                continue
            print()

    def show_invoice(self):
        inv=5004334
        print("\tCustomer Name: ",self.cus_name,end="\t\t")
        print("Invoic No. ",inv)
        inv+=1
        print(f"\tCode\t      Product\t  Price/Unit\t    Quqntity\t    Total\t")
        for i in Product.sold_products:
            for j in i:
                print(f"\t{j}\t",end="")
            print()
        print("------------------------------------------------------------------------------------------------")
        print("Total Amount: ",Product.total)


p1=Product()
while(True):
    print(" ------------------------------------------------------------------------------------------------------------------------")
    print("|\tPress 1: Add Product\tPress 2: Show Product\tPress 3: Create invoice\t Press 4: Show invoice\tPress 0: Exit\t|")
    print(" ------------------------------------------------------------------------------------------------------------------------")
    choice=int(input("Enter your choice: "))

    if choice == 1:
        print()
        p1.add()
        print()
    elif choice == 2:
        print()
        p1.display()
        print()
    elif choice == 3:
        print()
        p1.create_invoice()
        print()
    elif choice == 4:
        print()
        p1.show_invoice()
        print()
    elif choice == 0:
        exit()
    else:
        print("Wrong Choice!!!!!!!")