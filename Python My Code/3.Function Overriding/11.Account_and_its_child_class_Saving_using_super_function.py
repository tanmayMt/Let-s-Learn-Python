class Account:
    def __init__(self,acno,name,city,contact):
        self.acno=acno
        self.name=name
        self.city=city
        self.contact=contact
    def display(self):
        print("Account No. ",self.acno)
        print("Name: ",self.name)
        print("City: ",self.city)
        print("Contact: ",self.contact)

class Saving(Account):
    def __init__(self,acno,name,city,contact,actype):
        super().__init__(acno,name,city,contact)
        self.actype=actype
    def display(self):
        super().display()
        print("Type of account: ",self.actype)


# a=Account("50355565454","Bony Roy","Goa","8956337628")
# a.display()

# print()

s=Saving("453789689","Arohi Sen","Malbon","763487628","Saving")
s.display()

