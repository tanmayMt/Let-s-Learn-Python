class Mom:
    def eat(self):
        print("mom can eat")


class Baby(Mom):
    def eat(self):
        Mom.eat(self)
        print("Baby can eat")

b=Baby()
b.eat()


