product_list=[[1001,"Pencil",5],[1002,"Pen",3],[1003,"Bottle",30],[1004,"Tiffin",80]]
sold_list=[]
all_code=[]
for i in product_list:
    all_code.append(i[0])
print("List of Products Avlailable in Store")
print(f"\tCode\tProduct\t\tPrice/Unit\t")
for i in product_list:
    for j in i:
        print(f"\t{j}\t",end="")
    print()
print()
product_no=int(input("Enter Product No. "))
quantity=int(input("Enter Quantity: "))
if product_no in all_code:
    for i in product_list:
        if product_no==i[0]:
            item_price=i[2]*quantity
            i.append(item_price)
            sold_list.append(i)
else:
    print("Product is no avalible!!!!")

print(sold_list)
